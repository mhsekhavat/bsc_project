from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django_tables2 import tables, columns, A

from edu.models import Student, Professor
from edu.views.generic import TableView, EDUUpdateView, EDUDeleteView, EDUCreateView, create_basic_crud

user_views = create_basic_crud(
    User, 'staff_user',
    create_fields=['username', 'first_name', 'last_name'],
    edit_fields=['username', 'first_name', 'last_name'],
    list_fields=['username', 'first_name', 'last_name'],
    list_columns=dict(
        student=columns.Column(verbose_name='Student'),
        professor=columns.Column(verbose_name='Professor'),
    ),
    delete=True,
)

student_views = create_basic_crud(
    Student, 'staff_student',
    create_fields=['user'],
    list_fields=['id', 'user.username', 'user.first_name', 'user.last_name'],
    edit_fields=['user'],
    delete=True,
)

professor_views = create_basic_crud(
    Professor, 'staff_professor',
    create_fields=['user'],
    list_fields=['id', 'user.username', 'user.first_name', 'user.last_name'],
    edit_fields=['user'],
    delete=True,
)
