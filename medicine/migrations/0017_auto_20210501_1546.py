# Generated by Django 3.1.1 on 2021-05-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0016_auto_20210501_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cost_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='category',
            name='cost_without_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='category',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='sold_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='unit_price_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='category',
            name='unit_price_without_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]
