from edu.models import Student, Course, Offering, Professor
import factory
from factory import fuzzy


class StudentFactory(factory.Factory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class ProfessorFactory(factory.Factory):
    class Meta:
        model = Professor

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class CourseFactory(factory.Factory):
    class Meta:
        model = Course

    name = fuzzy.FuzzyText(length=8)
