from edu.models import Student, Course, Offering, Professor, Semester
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

    name = fuzzy.FuzzyText(length=8, prefix='Crs_')


class SemesterFactory(factory.Factory):
    class Meta:
        model = Semester

    name = fuzzy.FuzzyText(length=4, prefix='Sms_')


class OfferingFactory(factory.Factory):
    class Meta:
        model = Offering

    course = fuzzy.FuzzyChoice(Course.objects.all())
    semester = fuzzy.FuzzyChoice(Semester.objects.all())
    professor = fuzzy.FuzzyChoice(Professor.objects.all())
    capacity = fuzzy.FuzzyInteger(0, 10)

