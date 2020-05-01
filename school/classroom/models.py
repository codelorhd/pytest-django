from django.db import models
from django.utils.text import slugify

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_negative(value):
    if (value < 0):
        raise ValidationError(
            _("%(value)s is not a positive number"), params=("value", value),
        )


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)

    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(
        blank=True, null=TabError, validators=[validate_negative])

    username = models.SlugField(blank=True, null=True)

    def get_grade(self):
        if 0 <= self.average_score < 40:
            return 'fail'
        elif 40 <= self.average_score < 70:
            return 'pass'
        elif 70 <= self.average_score <= 100:
            return 'Excellent'
        else:
            return 'Error'

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.username = slugify(self.first_name)
        super(Student, self).save(*args, **kwargs)


class ClassRoom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField('classroom.Student')

    def __str__(self):
        return self.name
