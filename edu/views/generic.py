from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django_tables2 import RequestConfig, columns, A, Table


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
    create_url = None

    def get_queryset(self, **kwargs):
        return self.Table.Meta.model.objects.all()

    def get_table(self, **kwargs):
        table = self.Table(self.get_queryset(**kwargs))
        RequestConfig(self.request).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(TableView, self).get_context_data(**kwargs)
        context['table'] = self.get_table(**kwargs)
        context['create_url'] = self.create_url
        return context

    def get_page_title(self, **kwargs):
        return self.Table.Meta.model.__name__ + ' List'


class EDUUpdateView(PageTitleMixin, UpdateView):
    template_name = 'edu/form.html'

    def get_page_title(self, **kwargs):
        return 'Update %s' % self.model.__name__


class EDUCreateView(PageTitleMixin, CreateView):
    template_name = 'edu/form.html'

    def get_page_title(self, **kwargs):
        return 'Create %s' % self.model.__name__


class EDUDeleteView(PageTitleMixin, DeleteView):
    template_name = 'edu/confirm_delete.html'

    def get_page_title(self, **kwargs):
        return 'Delete %s' % self.model.__name__


def create_basic_crud(model, url_prefix,
                      create_fields=None,
                      list_fields=None,
                      edit_fields=None,
                      delete=None,
                      list_queryset=None,
                      list_columns=None,
                      ):
    views = {}
    model_name = model.__name__
    success_url = reverse_lazy(url_prefix + '_list') if list_fields is not None else '/'

    if create_fields is not None:
        views['create_view'] = type(
            model_name + 'CreateView',
            (EDUCreateView,),
            dict(
                model=model,
                fields=create_fields,
                success_url=success_url,
            )
        )
    if list_fields is not None:
        if list_queryset is None:
            def list_queryset(self, **kwargs):
                return model.objects.all()

        create_url = reverse_lazy(url_prefix + '_create') if create_fields is not None else None

        if list_columns is None:
            list_columns = dict()
        if edit_fields is not None and 'edit' not in list_columns:
            list_columns['edit'] = columns.LinkColumn(url_prefix + '_edit', kwargs={'pk': A('id')}, text='edit')
        if delete is not None and 'delete' not in list_columns:
            list_columns['delete'] = columns.LinkColumn(url_prefix + '_delete', kwargs={'pk': A('id')}, text='delete')

        views['list_view'] = type(
            model_name + 'ListView', (TableView,), dict(
                get_queryset=list_queryset,
                create_url=create_url,
                Table=type(
                    'Table', (Table,), dict(
                        Meta = type('Meta', tuple(), dict(
                            model = model,
                            fields = list_fields,
                        )),
                        **list_columns,
                    )
                )
            )
        )

    if edit_fields is not None:
        views['edit_view'] = type(
            model_name + 'EditView',
            (EDUUpdateView,),
            dict(
                model=model,
                fields=edit_fields,
                success_url=success_url,
            )
        )

    if delete:
        views['delete_view'] = type(
            model_name + 'DeleteView',
            (EDUDeleteView,),
            dict(
                model=model,
                success_url=success_url,
            )
        )
    return views
