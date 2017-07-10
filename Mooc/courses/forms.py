from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from .models import * 

class CourselistCreateForm(ModelForm):
    coursename = models.CharField(max_length=20, blank=True, null=True)
    coursedbname = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        model = Courselist
        fields = ['relationid','coursedbname','coursename']

class KeyWordCreateForm(ModelForm):
    stopword = models.CharField(max_length=10)
    class Meta:
        model = WordcloudStopword
        fields = ['stopword']
