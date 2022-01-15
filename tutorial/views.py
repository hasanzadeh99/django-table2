from django.shortcuts import render
from .models import Person
	
# tutorial/views.py
from django_tables2 import SingleTableView
from .tables import PersonTable


# class PersonListView(SingleTableView):
#     model = Person
#     table_class = PersonTable
#     template_name = 'tutorial/people.html'


# views.py
def person_list(request):
    table = PersonTable(Person.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=1)

    return render(request, 'tutorial/people.html', {
        "table": table
    })