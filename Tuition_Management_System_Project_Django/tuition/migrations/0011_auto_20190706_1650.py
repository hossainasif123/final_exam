# Generated by Django 2.2.2 on 2019-07-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0010_auto_20190706_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignee',
            name='to_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date finished'),
        ),
    ]