# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
                ('description', models.TextField(default='', blank=True)),
                ('image', models.ImageField(max_length=255, upload_to='product')),
                ('price', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
                'db_table': 'Product',
            },
        ),
    ]
