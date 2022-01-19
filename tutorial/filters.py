from django_filters import FilterSet

from .models import Person


class PersonFilter(FilterSet):
    class Meta:
        model = Person
        fields = {
                "alarm_data": ["exact"] , 
                "alarm_value": ["exact"] ,
                "Text": ["exact"] ,
                "alarm_type": ["exact"] ,
                "Group": ["exact"] , 
                "priority": ["exact"] ,
                "Acked_data": ["exact"] ,
                "Acked": ["exact"] ,
                  
                }

