# Generated by Django 3.1.1 on 2021-05-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0022_category_exp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='exp_date',
        ),
        migrations.AddField(
            model_name='purchaseinfo',
            name='exp_date',
            field=models.DateField(null=True),
        ),
    ]