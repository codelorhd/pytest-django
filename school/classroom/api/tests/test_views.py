from django.urls import reverse
from classroom.models import Student, ClassRoom
from rest_framework.test import APIClient
from django.test import TestCase
from mixer.backend.django import mixer
import pytest

pytestmark = pytest.mark.django_db


class Authentication:
    def get_client(self):
        self.client = APIClient()
        self.setAuthentication()
        return self.client

    def setAuthentication(self):
        from rest_framework.authtoken.models import Token
        from django.contrib.auth import get_user_model

        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="abcde")
        self.token = Token.objects.create(user=self.user).key

        # self.client.credentials(HTTP_CONTENTTYPE='application/json')
        self.token_url = "/api-token-auth/"

        user_data = {"username": "testuser", "password": "abcde"}
        response = self.client.post(self.token_url, data=user_data)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])


class TestStudentAPIViews(TestCase):
    def setUp(self):
        self.client = Authentication().get_client()

    def test_student_list_works(self):
        # create a student
        student = mixer.blend(Student, first_name="Solomon")
        student2 = mixer.blend(Student, first_name="Adeleke")

        # call the url
        response = self.client.get(reverse("student_list_api"))

        assert response.json != None
        assert len(response.json()) == 2
        assert response.status_code == 200

    def test_student_create_works(self):
        # data
        data = {
            "first_name": "SOLOMON",
            "last_name": "ABOYEJI",
            "admission_number": 1234,
            "is_qualified": True,
            "average_score": 100,
        }

        # call the url
        response = self.client.post(reverse("student_create_api"), data=data)

        assert response.json != None
        assert response.status_code == 201
        assert Student.objects.count() == 1
        assert response.data["username"] != ""

    def test_student_detail_works(self):
        student = mixer.blend(Student, first_name="Solomon")
        student2 = mixer.blend(Student, first_name="Adeleke")

        # call the url
        url = reverse("student_detail_api", kwargs={"pk": student.pk})
        url2 = reverse("student_detail_api", kwargs={"pk": student2.pk})

        response = self.client.get(url)
        response2 = self.client.get(url2)

        assert response.json != None
        assert response.status_code == 200
        assert response.json()["first_name"] == "Solomon"
        assert response.json()["username"] == "solomon"

        assert response2.json != None
        assert response2.status_code == 200
        assert response2.json()["first_name"] == "Adeleke"
        assert response2.json()["username"] == "adeleke"

    def test_student_delete_works(self):
        student = mixer.blend(Student, first_name="Solomon")
        assert Student.objects.count() == 1

        # call the url
        response = self.client.delete(
            reverse("student_delete_api", kwargs={"pk": student.pk})
        )

        assert response.status_code == 204
        assert Student.objects.count() == 0


class TestClassRoomAPIViews(TestCase):
    def setUp(self):
        self.client = Authentication().get_client()

    def test_classroom_qs_works(self):
        classrom_qs = mixer.blend(ClassRoom, student_capacity=20)
        classrom_qs2 = mixer.blend(ClassRoom, student_capacity=27)

        url = reverse("classroom_student_capacity_api", kwargs={"capacity": 20})

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["classroom_data"] != []
        assert response.data["number_classes"] == 2
