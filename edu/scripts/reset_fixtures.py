from django.contrib.auth import get_user_model

from edu.factory import StudentFactory, CourseFactory
from edu.models import Course, Student
from django.contrib.sessions.models import Session

def run():
    User = get_user_model()
    User.objects.all().exclude(username='admin')
    if not User.objects.filter(username='admin').exists:
        User.objects.create_superuser('admin', 'admin@admin.com', '321321')

    Course.objects.all().delete()
    courses = CourseFactory.create_batch(10)
    for c in courses:
        c.save()

    Student.objects.all().delete()
    students = StudentFactory.create_batch(10)
    for s in students:
        s.save()
