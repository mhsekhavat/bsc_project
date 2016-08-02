from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, RedirectView


class IndexView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user is None:
            return reverse('login')
        if hasattr(user, 'student'):
            return reverse('student')
        if hasattr(user, 'professor'):
            return reverse('professor')

        raise Exception('Neither Professor Nor Student')
