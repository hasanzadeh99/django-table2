# Generated by Django 3.2 on 2022-01-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='alarm_value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
