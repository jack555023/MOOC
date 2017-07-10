# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import (
    login, logout, update_session_auth_hash
)
from django.contrib.auth.views import login, password_change, password_change_done
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.response import TemplateResponse
from .forms import webUserForm,validForm,loginForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from flask import Flask, render_template, request, redirect




def login_view(request):
    if request.method == "POST":
        errors = []
        try:
            user = Webuser.objects.get(useremail= request.POST['useremail']+"@ntu.edu.tw")
        except ObjectDoesNotExist:
                user = None
        if user == None:
            errors.append("Invalid User_Name")
        else:
            if user.isvalid:
                if user.user_password == request.POST['user_password']:
                    print("Success")
                    request.session['User'] = user.useremail
                    return HttpResponseRedirect(reverse('courses:home'))
                else:
                    errors.append("Wrong Password ")
            else :
                    errors.append("User is not Valid")
    
        return render(request, 'registration/login.html', {
            'form':loginForm,
            'errors': errors,
        })
    
    else:
        form = loginForm()
        return render(request, 'registration/login.html', {
            'form':loginForm
        })



def logout_view(request):
    del request.session['User']
    return HttpResponseRedirect(reverse('courses:home'))


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserCreationForm()
#     return render_to_response(
#         "registration/sign_up.html",
#         {'form': form},
#         context_instance=RequestContext(request)
#     )


# @login_required
# def password_change_view(request):
#     return password_change(
#         request,
#         post_change_redirect='users:password_change_done'
#     )
def signup_view(request):
    errors = []
    if request.method == "POST":
        errors = []
        user_form = webUserForm(request.POST)
        if user_form.is_valid():
            if request.POST['user_password'] == request.POST['user_password2']:
                users = user_form.save()
                users.save()
                return HttpResponseRedirect('/')
            else:
                errors.append("PassWord is not consistent")
                return render(request, 'registration/sign_up.html', {
                    'form':webUserForm,
                    'errors': errors,
                })
    else:
        form = webUserForm()
        return render(request, 'registration/sign_up.html', {
            'form':webUserForm,
            'errors': errors,
        })



def valid_view(request):
    errors = []
    if request.method == "POST":    
        try:
            user = Webuser.objects.get(useremail= request.POST['useremail']+"@ntu.edu.tw")
        except ObjectDoesNotExist:
            user = None
        if user == None:
            errors.append("Invalid User_Name")
        else:
            if user.user_password == request.POST['user_password']:
                if user.valid_code == request.POST['valid_code']:
                    print("Success")
                    user.isvalid = True;
                    user.save();
                    return HttpResponseRedirect(reverse('courses:home'))
                else:
                    errors.append("Wrong Valid_Code ")
            else:
                errors.append("Wrong PassWord")
        
        return render(request, 'registration/valid.html', {
            'form':validForm,
            'errors': errors,
        })
        
    else:
        errors = []
        form = validForm()
        return render(request, 'registration/valid.html', {
            'form':validForm,
            'errors': errors,
        })


