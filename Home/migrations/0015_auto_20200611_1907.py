# Generated by Django 3.0.6 on 2020-06-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_timedeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timedeal',
            name='deal_name',
            field=models.CharField(help_text='This will display so it must be correct', max_length=50, verbose_name='Name Of the Deal'),
        ),
    ]
