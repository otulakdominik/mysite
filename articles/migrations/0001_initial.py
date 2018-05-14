# Generated by Django 2.0 on 2018-05-14 13:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateField(auto_now=True, verbose_name='modified')),
                ('pub_date', models.DateField(blank=True, null=True, verbose_name='published date')),
                ('comments_count', models.PositiveSmallIntegerField(default=0, verbose_name='comments count')),
                ('is_public', models.BooleanField(default=False, verbose_name='is public')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]