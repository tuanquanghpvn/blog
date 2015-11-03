# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
                ('description', models.TextField(default='', blank=True)),
                ('type', models.IntegerField(choices=[(1, 'Post'), (2, 'Product')], default=1)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
                'db_table': 'category',
            },
        ),
    ]
