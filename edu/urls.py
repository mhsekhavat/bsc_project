from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseForbidden
from django.views.generic.base import RedirectView, TemplateView
from functools import wraps
from edu.models import Student, Professor
from edu.views import index, student


def student_required(view):
    @login_required
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        try:
            kwargs['student'] = request.user.student
        except Student.DoesNotExist:
            return HttpResponseForbidden()
        return view(request, *args, **kwargs)

    return wrapper


def professor_required(view):
    @login_required
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        try:
            kwargs['professor'] = request.user.professor
        except Professor.DoesNotExist:
            return HttpResponseForbidden()
        return view(request, *args, **kwargs)

    return wrapper


student_urls = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('student_enrollments')), name='student'),
    url(r'^enrollments/$', student.EnrollmentListView.as_view(), name='student_enrollments')
]

professor_urls = [
    url(r'^$', TemplateView.as_view(template_name='edu/dashboard.html'), name='professor'),
]

urlpatterns = [
    url(r'^$', index.IndexView.as_view(), name='index'),
    url(r'^student/', decorator_include(student_required, student_urls)),
    url(r'^professor/', decorator_include(professor_required, professor_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^hijack/', include('hijack.urls')),
    url(r'^auth/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
