# Generated by Django 3.0.6 on 2020-06-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20200609_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_Discount_pricse',
            field=models.FloatField(max_length=30, null=True),
        ),
    ]
