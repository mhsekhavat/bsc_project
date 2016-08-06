from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.core.exceptions import ValidationError
from django.forms.fields import Field, ChoiceField
from django.forms.models import ModelForm, modelform_factory, ModelChoiceField
from django.forms.widgets import Widget
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django_tables2 import tables, columns

from edu.models import Enrollment, Offering, Semester, EnrollmentError
from edu.views.generic import TableView, create_basic_crud

enrollment_views = create_basic_crud(
    Enrollment, 'student_enrollment',
    list_fields=[],
    list_queryset=lambda self, student, **kwargs: student.enrollment_set.all(),
    list_columns=dict(
        semester=columns.Column(accessor='offering.semester.name', verbose_name='Semester'),
        course=columns.Column(accessor='offering.course.name', verbose_name='Course'),
        professor=columns.Column(accessor='offering.professor.user.last_name', verbose_name='Professor'),
    ),
    create_fields=[],
)

BasicEnrollmentCreateView = enrollment_views['create_view']


class EnrollmentCreateView(BasicEnrollmentCreateView, CreateView):
    fields = None

    def get_form_class(self):
        student = self.kwargs['student']

        class OfferingField(ModelChoiceField):
            def get_limit_choices_to(self):
                return dict(is_enrollable=True)

            def label_from_instance(self, obj):
                return '%s with %s' % (obj.course.name, obj.professor.user.last_name)

        class EnrollmentCreateForm(ModelForm):
            class Meta:
                model = Enrollment
                fields = ['offering']
                field_classes = dict(
                    offering=OfferingField,
                )

            def clean(self):
                cleaned_data = super(EnrollmentCreateForm, self).clean()
                offering = cleaned_data['offering']

                try:
                    offering.enroll(student, commit=False)
                except EnrollmentError as e:
                    raise ValidationError(e)
                return cleaned_data

            def save(self, commit=True):
                assert not self.errors
                return self.instance.offering.enroll(student, commit=commit)

        return EnrollmentCreateForm


enrollment_views['create_view'] = EnrollmentCreateView
