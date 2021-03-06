# Generated by Django 3.1.1 on 2021-04-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_auto_20210425_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='discount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='unit_price_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='unit_price_without_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, null=True),
        ),
    ]
