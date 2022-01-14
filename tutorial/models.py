# models.py
from django.contrib.auth import get_user_model
from django.db import models

class Person(models.Model):

    alarm_data=models.DateTimeField(verbose_name = 'alarm data')
    alarm_value=models.FloatField(verbose_name = 'alarm value')
    Text=models.CharField(max_length=500, verbose_name = 'Text')
    alarm_type=models.CharField(max_length=20, verbose_name= 'alarm type')
    Group=models.CharField(max_length=50, verbose_name= 'Group')
    priority=models.IntegerField(verbose_name='priority')
    Acked_data=models.DateTimeField(blank=True, null=True, verbose_name='acked data')
    Acked=models.BooleanField(default = False, verbose_name='acked' )
    


