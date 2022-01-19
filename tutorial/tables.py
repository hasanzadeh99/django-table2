# tutorial/tables.py
import django_tables2 as tables
from .models import Person

# class PersonTable(tables.Table):
#     class Meta:
#         model = Person
#         template_name = "django_tables2/bootstrap.html"
#         fields = ('__all__',)




# tables.py
import django_tables2 as tables
import django_filters

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class PersonTable(tables.Table):

    idd=tables.Column()
    iwe=CheckBoxColumnWithName(verbose_name=('Acked'), accessor='pk')
    delete = tables.LinkColumn('main:delete_item', args=[('pk')], attrs={'a': {'class': 'btn'}})

    class Meta:
        model = Person

        attrs = {'class': 'table table-striped table-bordered table-hover'}
        row_attrs = {'data-delivery': lambda record: record.Acked}        
        # attrs = {"class": "table table-hover table-sm",'backgroundColor': 'red'}
    # def __init__(self, *args, **kwargs):
    #     self.Column['c1'].Column.attrs = {"td":{"style" : "width:1%;" }}
        # self.columns['c2'].column.attrs = {"td":{"style" : "width:1%;" }}
        template_name = "django_tables2/bootstrap4.html"










data = [
    {"name": "Bradley"},
    {"name": "Stevie"},
]

class NameTable(tables.Table):
    name = tables.Column()

table = NameTable(data)