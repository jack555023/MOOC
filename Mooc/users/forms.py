from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from .models import * 
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import * 
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import random, string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
class webUserForm(ModelForm):
    class Meta:
        model = Webuser
        widgets = {
            'user_password': forms.PasswordInput(),
            'user_password2': forms.PasswordInput(),
        }
        user_password = models.CharField(max_length=45)
        user_password2 = models.CharField(max_length=45)
        fields = ['useremail','user_password','user_password2']

    def __init__(self, *args, **kwargs):
        super(webUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.fields['useremail'].label='EMail'
        self.fields['useremail'].help_text='請以臺灣大學Email註冊(Email 會成為ID)'    
        self.fields['user_password'].label='password'
        self.fields['user_password2'].label='password_confirm'  
        self.helper.layout = Layout(
            AppendedText('useremail','@ntu.edu.tw')
        )
        self.helper.add_input(Submit('submit', u'Sign Up', css_class="btn btn-primary text-center col-sm-12 User-btn")) 
    
    def save(self, commit=True):
        user = super(webUserForm, self).save(commit=False)
        valid_code = id_generator()
        account = str(self.cleaned_data["useremail"])
        user.useremail = self.cleaned_data["useremail"] + "@ntu.edu.tw"
        subject = "This is the validation Letter from NTU Moocs"
        to = user.useremail
        html_content = 'Click <a href ="http://140.112.107.63:8000/accounts/valid">  Here </a>  to active your accounts<br>'
        html_content = html_content + 'Your Validation Code is ' +  valid_code
        html_content = html_content + '<br><br> Ntu Moocs'
        msg = EmailMultiAlternatives(subject, to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        subject = "NTU MOOC 帳號申請"
        #to = "ntuticld@ntu.edu.tw"
        to = "jack555023@gmail.com"
        html_content = user.useremail + '此臺大帳號已申請MOOC帳號 '
        msg = EmailMultiAlternatives(subject, to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        user.isvalid = False
        user.valid_code = valid_code
        if commit:
            user.save()
        return user 


class validForm(forms.Form):
    useremail = forms.CharField(max_length=45)  # Field name made lowercase.
    user_password = forms.CharField(max_length=45,widget=forms.PasswordInput)
    valid_code = forms.CharField(max_length=45)
    class Meta:
        fields = ['useremail','user_password','valid_code']
    def __init__(self, *args, **kwargs):
        super(validForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.fields['useremail'].label='EMail'
        self.fields['user_password'].label='password' 
        self.fields['valid_code'].label='Validation_code'
        self.helper.layout = Layout(
            AppendedText('useremail','@ntu.edu.tw')
        )
        self.helper.add_input(Submit('submit', u'Validate', css_class="btn btn-primary text-center col-sm-12 User-btn")) 


class loginForm(forms.Form):
    useremail = forms.CharField(max_length=45)  # Field name made lowercase.
    user_password = forms.CharField(max_length=45,widget=forms.PasswordInput)
    class Meta:
        fields = ['useremail','user_password','valid_code']
    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.fields['useremail'].label='EMail' 
        self.fields['user_password'].label='password' 
        self.helper.layout = Layout(
            AppendedText('useremail','@ntu.edu.tw')
        )
        self.helper.add_input(Submit('submit', u'Log in', css_class="btn btn-primary text-center col-sm-12 User-btn")) 
