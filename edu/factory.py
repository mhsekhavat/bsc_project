from django.contrib.auth.models import User

from edu.models import Student, Course, Offering, Professor, Semester
import factory
from factory import fuzzy


class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Sequence(lambda n: 'user%d' % n)
    password = factory.Sequence(lambda n: 'pass%d' % n)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = model_class.objects
        # The default would use ``manager.create(*args, **kwargs)``
        return manager.create_user(*args, **kwargs)


class StudentFactory(factory.Factory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)


class ProfessorFactory(factory.Factory):
    class Meta:
        model = Professor

    user = factory.SubFactory(UserFactory)


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
