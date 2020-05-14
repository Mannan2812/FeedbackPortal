from django.shortcuts import render,redirect,HttpResponseRedirect,reverse,HttpResponse
from .forms import RegisterForm,ProfileForm
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from authenticate.models import User,UserProfile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
import os

# Create your views here.
def login_user(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        login_state = (request.POST.get('login_state'))
        user  = authenticate(email = email,password = password)
        if user is not None:
            if not UserProfile.objects.filter(user = user).exists():
                login(request,user)
                return redirect('authenticate:edit_profile')
            elif user.category==login_state:
                profile = UserProfile.objects.get(user = user)
                pro= user.date_joined
                d = datetime.date.today()
                profile.year = ((d.year  -(int)(pro.year))*12 + (d.month-(pro.month)))//6+1
                profile.save()
                print('logged in')
                login(request,user)
                # print(User.objects.get_queryset().filter(email = email).group)
                return redirect('home:homepage')
            else:
                print('user is not authenticated')
                messages.info(request,'Wrong Email or Password!')
                return redirect('authenticate:login')
        else:
            print('user is not authenticated')
            messages.info(request,'Wrong Email or Password!')
            return redirect('authenticate:login')
    else:
        if request.user is not None:
            logout(request)
        return render(request,'authenticate/index.html')

def logout_user(request):
    logout(request)
    return redirect('authenticate:login')

def register(request):
    form = RegisterForm()
    return render(request,'authenticate/register.html',{'form':form})

@login_required(login_url = reverse_lazy('authenticate:login'))#,kwargs= {'not_logged_in':'You need to login first to access dashboard'}))
def edit_profile(request):
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            if not UserProfile.objects.filter(user=request.user).exists():
                profile = form.save(commit = False)
                profile.user = request.user
                profile.save()
                user = request.user
                user.name = profile.name;
                user.save()
            else:
                path2 = settings.MEDIA_ROOT+'\\profile_pic\\'
                mail= str(request.user.email).replace('@','')
                path2 = path2+ mail+'.png'
                os.remove(path2)
                profile = UserProfile.objects.get(user = request.user)
                profile.name = form.cleaned_data['name']
                profile.profile_pic= form.cleaned_data['profile_pic']
                profile.save()
                user = request.user
                user.name = profile.name;
                user.save()


            # profile.name = form.cleaned_data.get('name')
            # profile.profile_pic = request.FILES['profile_pic']
            # profile.save()
            return redirect('home:homepage')
    form = ProfileForm()
    if UserProfile.objects.filter(user=request.user).exists():
        return render(request,'authenticate/profile.html',{'form':form,'year':UserProfile.objects.get(user = request.user).year})
    else:
        return render(request,'authenticate/profile.html',{'form':form})
