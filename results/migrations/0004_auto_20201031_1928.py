# Generated by Django 3.1.2 on 2020-10-31 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20201031_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billresults',
            name='number',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='billresults',
            name='title',
            field=models.CharField(default=None, max_length=300, unique=True),
        ),
    ]
