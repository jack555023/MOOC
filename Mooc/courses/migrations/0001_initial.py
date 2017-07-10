# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courselist',
            fields=[
                ('relationid', models.AutoField(primary_key=True, serialize=False, db_column='relationId')),
                ('webuser', models.CharField(max_length=45, db_column='webUser')),
                ('coursedbname', models.CharField(max_length=45, db_column='courseDBName')),
                ('coursename', models.CharField(max_length=45, db_column='courseName')),
            ],
            options={
                'managed': False,
                'db_table': 'courselist',
            },
        ),
    ]
