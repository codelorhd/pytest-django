from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)

    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=TabError)

    def get_grade(self):
        if self.average_score < 40:
            return 'fail'
        elif 40 < self.average_score < 70:
            return 'pass'
        elif 70 < self.average_score <= 100:
            return 'Excellent'
        else:
            return 'Error'

    def __str__(self):
        return self.first_name


class ClassRoom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    student = models.ManyToManyField('classroom.Student')

    def __str__(self):
        return self.name
