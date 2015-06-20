# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anli',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('discriptions', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('descriptions', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CateBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('discriptions', models.CharField(max_length=150, null=True, blank=True)),
                ('blog', models.ForeignKey(related_name='blog', to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='case',
            name='jinjis',
        ),
        migrations.RemoveField(
            model_name='case',
            name='xinshis',
        ),
        migrations.DeleteModel(
            name='Case',
        ),
        migrations.RemoveField(
            model_name='jinji',
            name='pictures',
        ),
        migrations.DeleteModel(
            name='Jinji',
        ),
        migrations.RemoveField(
            model_name='xinshi',
            name='pictures',
        ),
        migrations.DeleteModel(
            name='Xinshi',
        ),
        migrations.AddField(
            model_name='anli',
            name='case',
            field=models.ForeignKey(related_name='case', to='blog.Cases'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='discription',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='address',
            field=models.CharField(default='sss', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='weiboimg',
            field=models.ImageField(default='aasas', upload_to=b'photos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='tel',
            field=models.IntegerField(max_length=15),
            preserve_default=True,
        ),
    ]
