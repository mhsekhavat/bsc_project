from django.db import models


class Course(models.Model):
    pass


class Student():
    def get_max_units(self):
        pass


class Professor():
    pass


class Offering(models.Model):
    course = models.ForeignKey(Course)
    # time = models.time
    semester = models.ForeignKey(Semester)
    professor = models.ForeignKey(Professor)


class Enrollment(models.Model):
    pass


class Semester(models.Model):
    pass
