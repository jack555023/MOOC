
# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class Courselist(models.Model):
    relationid = models.AutoField(db_column='relationId', primary_key=True)  # Field name made lowercase.
    webuser = models.CharField(db_column='webUser', max_length=45)  # Field name made lowercase.
    coursedbname = models.CharField(db_column='courseDBName', max_length=45)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courselist'

class WordcloudStopword(models.Model):
    db_name = models.CharField(db_column='DB_name', max_length=255)  # Field name made lowercase.
    stopword = models.CharField(max_length=10)
    lasttimemodified = models.DateTimeField(db_column='lastTimeModified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wordcloud_stopword'



class CourseOverviews(models.Model):
    course_name = models.CharField(db_column='Course_name', max_length=55,primary_key=True)  # Field name made lowercase.
    course_code = models.CharField(db_column='Course_code', max_length=255)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    instructor = models.CharField(db_column='Instructor', max_length=255)  # Field name made lowercase.
    open_date = models.DateField(db_column='Open date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    close_date = models.DateField(db_column='Close Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    op = models.CharField(db_column='OP', max_length=255)  # Field name made lowercase.
    ac = models.CharField(db_column='AC', max_length=255)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=255)  # Field name made lowercase.
    update_date = models.DateField(db_column='Update_date')  # Field name made lowercase.
    renew = models.IntegerField(db_column='Renew')  # Field name made lowercase.
    total_visitors = models.IntegerField(db_column='Total_Visitors')  # Field name made lowercase.
    total_enrolled_learners = models.IntegerField(db_column='Total_Enrolled_Learners')  # Field name made lowercase.
    enroll_learner_rate = models.FloatField(db_column='Enroll_Learner_Rate')  # Field name made lowercase.
    active_learners = models.IntegerField(db_column='Active_Learners')  # Field name made lowercase.
    active_learners_rate = models.FloatField(db_column='Active_Learners_Rate')  # Field name made lowercase.
    course_completers = models.IntegerField(db_column='Course_Completers')  # Field name made lowercase.
    course_completer_rate = models.IntegerField(db_column='Course_Completer_Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course_overviews'



