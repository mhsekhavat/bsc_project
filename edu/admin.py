from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from hijack_admin.admin import HijackUserAdmin

from edu.models import Course, Student, Offering, Professor, Enrollment, Semester

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Offering)
admin.site.register(Professor)
admin.site.register(Enrollment)
admin.site.register(Semester)


class EDUUserAdmin(HijackUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'student', 'professor', 'hijack_field')


admin.site.unregister(User)
admin.site.register(User, EDUUserAdmin)
