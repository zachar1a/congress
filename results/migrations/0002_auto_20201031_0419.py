# Generated by Django 3.1.2 on 2020-10-31 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billresults',
            name='Result',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]