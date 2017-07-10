# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webuser',
            fields=[
                ('userid', models.AutoField(db_column='userId', serialize=False, primary_key=True)),
                ('useremail', models.CharField(max_length=45, db_column='userEmail', unique=True)),
                ('user_password', models.CharField(max_length=45)),
                ('user_password2', models.CharField(max_length=45)),
                ('isvalid', models.CharField(null=True, max_length=45, blank=True)),
                ('valid_code', models.CharField(null=True, max_length=45, blank=True)),
            ],
            options={
                'db_table': 'webuser',
                'managed': False,
            },
        ),
    ]
