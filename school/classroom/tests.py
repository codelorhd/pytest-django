from django.test import TestCase
from classroom.models import Student

from mixer.backend.django import mixer


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
        # Student.ojects.create(
        #     first_name='SOLOMON',
        #     last_name='ADELEKE',
        #     admission_number=1234
        # )
        student1 = mixer.blend(Student, first_name='SOLOMON')

        student_result = Student.objects.last()
        assert student_result.first_name == 'SOLOMON'

    def test_str_returns(self):
        student1 = mixer.blend(Student, first_name='SOLOMON')
        student_result = Student.objects.last()
        assert str(student1) == 'SOLOMON'

    def test_grade_fail(self):
        student1 = mixer.blend(Student, average_score=10)
        student_result = Student.objects.last()
        assert student_result.get_grade() == 'fail'

    def test_grade_pass(self):
        student1 = mixer.blend(Student, average_score=60)
        student_result = Student.objects.last()
        assert student_result.get_grade() == 'pass'

    def test_grade_excellent(self):
        student1 = mixer.blend(Student, average_score=90)
        student_result = Student.objects.last()
        assert student_result.get_grade() == 'Excellent'
