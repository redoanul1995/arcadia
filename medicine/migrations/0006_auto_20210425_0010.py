# Generated by Django 3.1.1 on 2021-04-25 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_auto_20210425_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='actual_cost',
            new_name='cost_with_discount',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='total_cost',
            new_name='cost_without_discount',
        ),
    ]
