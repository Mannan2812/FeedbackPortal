from django import forms
from .models import User,UserProfile,Feedback,upload_to_rename
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    first_name = forms.CharField(max_length = 100,required =True)
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
class CustomPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = 'Old Password',widget = forms.PasswordInput(attrs = {
    'class':'form-control',
    'placeholder':'Old Password',
    'style':'display:inline-block;width:auto;'
    }))
    new_password1 = forms.CharField(label= "New Password",widget = forms.PasswordInput(attrs = {
    'class':'form-control',
    'placeholder':'New Password',
    'style':'display:inline-block;width:auto;'
    }))
    new_password2 = forms.CharField(label = "Retype new Password",widget = forms.PasswordInput(attrs = {
    'class':'form-control',
    'placeholder':'Password again',
    'style':'display:inline-block;width:auto;'
    }))
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length = "254",widget = forms.TextInput(attrs = {
    'class':'form-control',
    'placeholder':'Enter you email id',
    'style':'display:inline-block;width:auto;'
    }),required = True)
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs= {
    'class':'form-control',
    'placeholder':'Enter your new Password',
    'style':'display:inline-block;width:auto;'
    }),required= True,label = "Enter New Password")
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs= {
    'class':'form-control',
    'placeholder':'Enter your Password again',
    'style':'display:inline-block;width:auto;'
    }),required= True,label = "Enter your Password again")
YEAR_CHOICES = (('Select Current Year',(
    ("1","1st Year"),
    ("2","2nd Year"),
    ("3","3rd Year"),
    ("4","4th Year"),
    )),)

class ProfileForm(forms.ModelForm):
    name = forms.CharField(widget =forms.TextInput(attrs = {
    'class':'form-control',
    "id":'inputGroupSelect04',
    "placeholder" : "Enter your name",
    "style":'height:60px;'
    }));
    year = forms.CharField(widget =forms.TextInput(attrs = {
    'class':'form-control',
    "id":'inputGroupSelect04',
    "placeholder" : "Year",
    "style":'height:60px;background-color:white;',
    "readonly":'',
    "value":'1',
    }));
    branch = forms.CharField(widget =forms.TextInput(attrs = {
    'class':'form-control',
    "id":'inputGroupSelect04',
    "placeholder" : "Year",
    "style":'height:60px;background-color:white;',
    "value":"To be updated",
    "readonly":'',
    }));
    # profile_pic = forms.ImageField(upload_to = upload_to_rename,required = False,widget = forms.ClearableFileInput(attrs = {
    # 'class':'custom-file-input',
    # 'id':'inputGroupFile03',
    # }))
    class Meta:
        model = UserProfile
        fields = ('name','year','branch','profile_pic')

OPTIONS_CHOICES = (
(1,"Very Bad"),
(2,"Bad"),
(3,"Neutral"),
(4,"Good"),
(5,"Very Good"),

)
class FeedbackForm(forms.ModelForm):
    que1 = forms.ChoiceField(required = True,choices = OPTIONS_CHOICES,widget = forms.RadioSelect(attrs = {'class':"classname",'id':'options_choice_1'}))
    que2 = forms.ChoiceField(required = True,choices = OPTIONS_CHOICES,widget = forms.RadioSelect(attrs = {'class':"classname",'id':'options_choice_2'}))
    que3 = forms.ChoiceField(required = True,choices = OPTIONS_CHOICES,widget = forms.RadioSelect(attrs = {'class':"classname",'id':'options_choice_3'}))
    que4 = forms.ChoiceField(required = True,choices = OPTIONS_CHOICES,widget = forms.RadioSelect(attrs = {'class':"classname",'id':'options_choice_4'}))
    que5 = forms.ChoiceField(required = True,choices = OPTIONS_CHOICES,widget = forms.RadioSelect(attrs = {'class':"classname",'id':'options_choice_5'}))
    comment = forms.CharField(required=False,widget = forms.Textarea(attrs = {'placeholder':'Type you comment here','id':'comments','rows':7,'class':'form-control'}))
    class Meta:
        model = Feedback
        fields = ('que1','que2','que3','que4','que5','comment')
