# Generated by Django 2.0 on 2018-05-16 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180514_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Entry'),
        ),
    ]
