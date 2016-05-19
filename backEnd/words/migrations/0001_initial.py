# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('definition', models.TextField()),
                ('language', models.CharField(choices=[('en', 'English'), ('kk', 'Kazakh'), ('ru', 'Russian')], max_length=5)),
                ('antonyms', models.ManyToManyField(blank=True, related_name='_word_antonyms_+', to='words.Word')),
                ('synonyms', models.ManyToManyField(blank=True, related_name='_word_synonyms_+', to='words.Word')),
                ('translation', models.ManyToManyField(blank=True, related_name='_word_translation_+', to='words.Word')),
            ],
        ),
    ]
