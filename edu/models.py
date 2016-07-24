from django.db import models
from django.apps import apps

from insanity.action import action


class Course(models.Model):
    name = models.CharField(max_length=32)


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def get_max_units(self):
        pass

    def current_semester_units(self):
        pass


class Professor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Offering(models.Model):
    course = models.ForeignKey('edu.Course')
    # time = models.time
    semester = models.ForeignKey('edu.Semester')
    professor = models.ForeignKey('edu.Professor')
    capacity = models.IntegerField()

    @action
    def enroll(self, student):
        if self.capacity == 0:
            return False
        Enrollment = apps.get_model('edu.Enrollment')
        Enrollment.objects.create(offering=self, student=student)
        self.capacity = self.capacity - 1
        self.save()
        return True

    @action
    def get_students(self):
        return Student.objects.filter(id__in=self.enrollment_set.values_list('student', flat=True))


class Enrollment(models.Model):
    offering = models.ForeignKey('edu.Offering')
    student = models.ForeignKey('edu.Student')


class Semester(models.Model):
    name = models.CharField(max_length=16)
