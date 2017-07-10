from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from flask import Flask, render_template, request, redirect
import time

# Create your views here.


def home(request):
    popular_list = Courselist.objects.order_by('coursename')
    if 'User' in request.session:
        username = request.session['User']
        print(request.session['User'])
        print("User_in")
        username = username.split('@')[0]
        own_list = Courselist.objects.filter(**{'webuser': username})
        print(own_list)
        return render(request, 'home.html', {
            'own_list': own_list,
            'popular_list': popular_list
        })
    else:
        return render(request, 'home.html', {
            'popular_list': popular_list
        })


def addcourses(request):
    if request.method == "POST":
        createCourse_form = CourselistCreateForm(request.POST)
        if createCourse_form.is_valid():
            course = createCourse_form.save()
            course.webuser = request.user.username
            course.save()
            return HttpResponseRedirect('/')
    else:
        form = CourselistCreateForm()
        return render(request, 'addcourses.html', {
            'form':CourselistCreateForm
        })


def keywords(request,pk):
    course = Courselist.objects.filter(**{'relationid': pk})
    db_name = course[0].coursedbname
    print(db_name)
    word_list = WordcloudStopword.objects.filter(**{'db_name': db_name })  
    print(word_list)
    return render(request, 'keyword.html', {
        'db_number': pk,
        'word_list': word_list,
    })
    

def deleteCourses(request,pk):
    course = Courselist.objects.filter(**{'relationid': pk})
    course.delete()
    return HttpResponseRedirect('/')

def deletekeywords(request,pk):
    keyword = WordcloudStopword.objects.filter(**{'id': pk})
    keyword.delete()
    return HttpResponseRedirect('/')

def addkeywords(request,pk):
    if request.method == "POST":
        keyword_form = KeyWordCreateForm(request.POST)
        if keyword_form.is_valid():
            keyword = keyword_form.save()
            course = Courselist.objects.filter(**{'relationid': pk})
            db_name = course[0].coursedbname
            keyword.db_name = db_name
            keyword.lasttimemodified ='2017-01-01 12:00:00'
            print(time.time())
            keyword.save()
            return HttpResponseRedirect('/keywords/'+pk+'/')
    else:
        form = KeyWordCreateForm()
        return render(request, 'addkeywords.html', {
            'form':KeyWordCreateForm
        })