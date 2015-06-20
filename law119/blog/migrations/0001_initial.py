# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=5000)),
                ('author', models.CharField(max_length=50)),
                ('public_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('LeiXing', models.CharField(max_length=1, choices=[(b'J', b'jinji'), (b'X', b'xinshis')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=15)),
                ('web', models.URLField()),
                ('email', models.EmailField(max_length=75)),
                ('weibo', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jinji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Xinshi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=5000)),
                ('pictures', models.ManyToManyField(to='blog.Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='jinji',
            name='pictures',
            field=models.ManyToManyField(to='blog.Picture'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='jinjis',
            field=models.ManyToManyField(to='blog.Jinji'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='xinshis',
            field=models.ManyToManyField(to='blog.Xinshi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='about_us',
            name='picture',
            field=models.ManyToManyField(to='blog.Picture'),
            preserve_default=True,
        ),
    ]
