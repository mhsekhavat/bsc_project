from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.forms.models import ModelForm
from django.views.generic.edit import UpdateView
from django_tables2 import columns, A

from edu.models import Student, Professor, Course, Semester, Offering, ChangeCapacityError
from edu.views.generic import create_basic_crud
from insanity.action import action

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

course_views = create_basic_crud(
    Course, 'staff_course',
    create_fields=['name'],
    list_fields=['id', 'name'],
    edit_fields=['name'],
    delete=True,
)

semester_views = create_basic_crud(
    Semester, 'staff_semester',
    create_fields=['name'],
    list_fields=['id', 'name'],
    edit_fields=['name'],
    delete=True,
)

offering_views = create_basic_crud(
    Offering, 'staff_offering',
    create_fields=['semester', 'course', 'professor', 'capacity'],
    list_fields=[],
    list_columns=dict(
        semester=columns.Column(accessor='semester.name', verbose_name='Semester'),
        course=columns.Column(accessor='course.name', verbose_name='Course'),
        professor=columns.Column(accessor='professor.user.last_name', verbose_name='Professor'),
        capacity=columns.Column(accessor='capacity', verbose_name='Capacity'),
        _capacity=columns.LinkColumn('staff_offering_capacity', kwargs={'pk': A('id')}, text='change'),
        available_capacity=columns.Column(accessor='available_capacity', verbose_name='Available Capacity'),
        is_enrollable=columns.BooleanColumn(accessor='is_enrollable', verbose_name='Enrollable'),
    ),
    edit_fields=['semester', 'course', 'professor', 'is_enrollable'],
    delete=True,
)


class OfferingChangeCapacityView(UpdateView):
    model = Offering
    template_name = 'edu/form.html'
    success_url = reverse_lazy('staff_offering_list')

    def get_form_class(self):
        class ChangeCapacityForm(ModelForm):
            class Meta:
                fields = ['capacity']
                model = Offering

            def clean(self):
                cleaned_data = super(ChangeCapacityForm, self).clean()
                new_capacity = cleaned_data['capacity']
                try:
                    self.instance.change_capacity(new_capacity, commit=False)
                except ChangeCapacityError as e:
                    raise ValidationError(e)

            def save(self, commit=True):
                new_capacity = self.instance.capacity
                with action('myContextAction', offering=self.instance):
                    self.instance.change_capacity(new_capacity, commit=commit)
                return self.instance

        return ChangeCapacityForm
