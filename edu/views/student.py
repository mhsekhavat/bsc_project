from django_tables2 import tables, columns

from edu.models import Enrollment
from edu.views.generic import TableView


class EnrollmentListView(TableView):
    def get_queryset(self, student, **kwargs):
        # TODO: read student from request
        return student.enrollment_set.all()

    class Table(tables.Table):
        class Meta:
            model = Enrollment
            fields = tuple()

        semester = columns.Column(accessor='offering.semester.name', verbose_name='Semester')
        course = columns.Column(accessor='offering.course.name', verbose_name='Course')
        professor = columns.Column(accessor='offering.professor.user.last_name', verbose_name='Professor')
