# Generated by Django 3.1.1 on 2021-04-30 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_auto_20210430_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='adding_date',
        ),
    ]
