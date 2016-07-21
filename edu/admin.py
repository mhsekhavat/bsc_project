from django.contrib import admin

from edu.models import Course, Student, Offering, Professor, Enrollment, Semester

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Offering)
admin.site.register(Professor)
admin.site.register(Enrollment)
admin.site.register(Semester)
