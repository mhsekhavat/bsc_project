from django.views.generic import TemplateView
from django_tables2 import RequestConfig


class PageTitleMixin(object):
    page_title = 'untitled'

    def get_context_data(self, **kwargs):
        context = super(PageTitleMixin, self).get_context_data(**kwargs)
        context['page_title'] = self.get_page_title(**kwargs)
        return context

    def get_page_title(self, **kwargs):
        return self.page_title


class TableView(PageTitleMixin, TemplateView):
    Table = NotImplemented
    template_name = 'edu/list_table.html'

    def get_queryset(self, **kwargs):
        return self.Table.Meta.model.objects.all()

    def get_table(self, **kwargs):
        table = self.Table(self.get_queryset(**kwargs))
        RequestConfig(self.request).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(TableView, self).get_context_data(**kwargs)
        context['table'] = self.get_table(**kwargs)
        return context

    def get_page_title(self, **kwargs):
        return self.Table.Meta.model.__name__ + ' List'
