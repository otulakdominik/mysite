# Generated by Django 2.0 on 2018-05-14 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]