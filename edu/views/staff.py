from django.core.urlresolvers import reverse_lazy
from django_tables2 import tables, columns

from edu.models import Student
from edu.views.generic import TableView


class StudentListView(TableView):
    def get_queryset(self, **kwargs):
        # TODO: read student from request
        return Student.objects.all()

    create_url = reverse_lazy('index')

    class Table(tables.Table):
        class Meta:
            model = Student
            fields = ('id', 'user.first_name', 'user.last_name', 'user.username')
