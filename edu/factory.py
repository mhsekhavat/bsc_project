from edu.models import Student, Course, Offering
import factory

class StudentFactory(factory.Factory):
    class Meta:
        model = Student
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

class CourseFactory(factory.Factory):
