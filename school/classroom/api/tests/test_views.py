from django.urls import reverse
from classroom.models import Student, ClassRoom
from rest_framework.test import APIClient
from django.test import TestCase
from mixer.backend.django import mixer
import pytest
pytestmark = pytest.mark.django_db


class TestStudentAPIViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        print(self.client, "self.client")

    def test_student_list_works(self):
        # create a student
        student = mixer.blend(Student, first_name="Solomon")
        student2 = mixer.blend(Student, first_name="Adeleke")

        # call the url
        response = self.client.get(reverse('student_list_api'))

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
        response = self.client.post(reverse('student_create_api'), data=data)

        assert response.json != None
        assert response.status_code == 201
        assert Student.objects.count() == 1
        assert response.data['username'] != ''

    def test_student_detail_works(self):
        student = mixer.blend(Student, first_name="Solomon")
        student2 = mixer.blend(Student, first_name="Adeleke")

        # call the url
        url = reverse('student_detail_api', kwargs={
            "pk": 1
        })
        url2 = reverse('student_detail_api', kwargs={
            "pk": 2
        })

        response = self.client.get(url)
        response2 = self.client.get(url2)

        assert response.json != None
        assert response.status_code == 200
        assert response.json()['first_name'] == 'Solomon'
        assert response.json()['username'] == 'solomon'

        assert response.json != None
        assert response.status_code == 200
        assert response2.json()['first_name'] == 'Adeleke'
        assert response2.json()['username'] == 'adeleke'

    def test_student_delete_works(self):
        student = mixer.blend(Student, first_name="Solomon")
        assert Student.objects.count() == 1

        # call the url
        response = self.client.delete(reverse('student_delete_api', kwargs={
            "pk": 1
        }))

        assert response.status_code == 204
        assert Student.objects.count() == 0
