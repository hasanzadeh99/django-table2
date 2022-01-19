from mmap import PAGESIZE
from django.shortcuts import render
from .models import Person,Staff
	
# tutorial/views.py
from django_tables2 import SingleTableView
from .tables import PersonTable


# class PersonListView(SingleTableView):
#     model = Person
#     table_class = PersonTable
#     template_name = 'tutorial/people.html'


# views.py
# def person_list(request):
#     table = PersonTable(Person.objects.all())
#     table.paginate(page=request.GET.get('page', 1), per_page=10)
#     filterset_class = PersonFilter
#     return render(request, 'tutorial/people.html', {
#         "table": table
#     })


from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import PersonFilter


# class FilteredPersonListView(SingleTableMixin, FilterView):
#     table_class = PersonTable
#     model = Person
#     template_name = "template.html"

from django_tables2.export.views import ExportMixin
from django.shortcuts import get_object_or_404, render
from django_tables2 import LazyPaginator
  

class FilteredPersonListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    template_name = "bootstrap4_template.html"

    filterset_class = PersonFilter

    export_formats = ("csv", "xls")

    def get_table_kwargs(self):
        return {"template_name": "django_tables2/bootstrap.html"}


from listable.views import BaseListableView



class StaffList(BaseListableView):

    model = Staff

    fields = ("Group",)
    # widgets = {...} # optional
    # search_fields = {...} # optional
    # order_fields = {...} # optional
    # headers = {...} # optional
    # select_related = (...) # optional
    # prefetch_related = (...) # optional
    # order_by = (...) # optional

    def generic(self, obj):
        return obj.generic_object.name

    def name(self, staff):
        return staff.name()

    def get_extra(self):
        cta = ContentType.objects.get_for_model(models.GenericModelA)
        ctb = ContentType.objects.get_for_model(models.GenericModelB)

        extraq = """
        CASE
            WHEN content_type_id = {0}
                THEN (SELECT name from staff_genericmodela WHERE object_id = staff_genericmodela.id)
            WHEN content_type_id = {1}
                THEN (SELECT name from staff_genericmodelb WHERE object_id = staff_genericmodelb.id)
        END
        """.format(cta.pk, ctb.pk)

        return {"select": {'genericname': extraq}}