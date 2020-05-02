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
