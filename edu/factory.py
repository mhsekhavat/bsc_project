from edu.models import Student, Course, Offering
import factory
from factory import fuzzy


class StudentFactory(factory.Factory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class CourseFactory(factory.Factory):
    class Meta:
        model = Course

    name = fuzzy.FuzzyText()
