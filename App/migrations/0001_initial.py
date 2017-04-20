# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProfile',
            fields=[
                ('pname', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('ppassword', models.CharField(max_length=100)),
                ('pabout', models.CharField(max_length=160)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unique_id', models.CharField(default=b'00000000', max_length=8)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='projectID',
            field=models.ForeignKey(to='App.ProjectProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='userID',
            field=models.ForeignKey(to='App.UserProfile'),
            preserve_default=True,
        ),
    ]
