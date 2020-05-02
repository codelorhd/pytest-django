from django.test import TestCase
import pytest

from hypothesis import strategies as st, given
from hypothesis.extra.django import TestCase

from .models import Student, ClassRoom

from mixer.backend.django import mixer

# prevents pytest from data to the database
pytestmark = pytest.mark.django_db


class TestStudentModel(TestCase):

    # def setUp(self):
    # self.student1 = Student.objects.create(
    #     first_name='SOLOMON',
    #     last_name='ADELEKE',
    #     admission_number=12345
    # )

    def test_add_a_plus_b(self):
        a = 1
        b = 2

        c = a + b
        assert c == 3

    def test_student_can_be_created(self):
        student1 = mixer.blend(Student, first_name='SOLOMON')

        student_result = Student.objects.last()
        assert student_result.first_name == 'SOLOMON'

    def test_str_returns(self):
        student1 = mixer.blend(Student, first_name='SOLOMON')
        student_result = Student.objects.last()
        assert str(student1) == 'SOLOMON'

    # @given(st.characters())
    # def test_slugify(self, name):
    #     print(name, "name")
    #     student1 = mixer.blend(Student, first_name=name)
    #     student1.save()
        
    #     student_result = Student.objects.last()
    #     assert len(str(student_result.username)) == len(name)

    @given(st.floats(max_value=40, min_value=0))
    def test_grade_fail(self, fail_score):
        print(fail_score, "this is the fail score")
        student1 = mixer.blend(Student, average_score=fail_score)
        student_result = Student.objects.last()
        assert student_result.get_grade() == 'fail'

    @given(st.floats(max_value=70, min_value=40))
    def test_grade_pass(self, score):
        print(score, "score is ")
        student1 = mixer.blend(Student, average_score=score)
        student_result = Student.objects.last()
        assert student_result.get_grade() == 'pass'

    @given(st.floats(max_value=100, min_value=71))
    def test_grade_excellent(self, score):
        student1 = mixer.blend(Student, average_score=score)
        student_result = Student.objects.last()
        assert student_result.get_grade() == 'Excellent'

    @given(st.floats(min_value=100.1, max_value=200))
    def test_grade_error(self, score):
        print(score, "is score")
        student1 = mixer.blend(Student, average_score=score)
        student_result = Student.objects.last()
        assert student_result.get_grade() == 'Error'


class TestClassRoomModel():
    def test_classroom_create(self):
        classroom = mixer.blend(ClassRoom, name="Physics")
        classroom_result = ClassRoom.objects.last()
        assert str(classroom_result) == 'Physics'
