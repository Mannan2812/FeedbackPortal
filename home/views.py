from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from authenticate.views import login_user
from authenticate.forms import FeedbackForm
from authenticate.models import FeedbackTile,SEMESTER_COURSES,UserProfile,Feedback,User
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.conf import settings
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
from os import path
# Create your views here.
@login_required(login_url = reverse_lazy('authenticate:login'))#,kwargs= {'not_logged_in':'You need to login first to access dashboard'}))
def HomePage(request,message = 'default'):
    context = dict()
    if message!='default':
        context['message'] = message
    if request.user.category =="Student":
        profile = UserProfile.objects.get(user = request.user)
        var = profile.branch+profile.year
        feedback_list = list()
        list_filled = list()
        if profile.feedback_filled is None:
            list_filled.append('HEY')
        else:
            list_filled = profile.feedback_filled.split(' ')
        for i in SEMESTER_COURSES[var]:
            if i not in list_filled:
                feedbacktile = FeedbackTile.objects.filter(course_code = i)
                if len(feedbacktile) > 0:
                    feedback_list.append(feedbacktile[0])

        img_name = request.user.email
        img_name = img_name.replace('@','')+'.png'
        path2 = settings.MEDIA_ROOT+'\\profile_pic\\'
        if not path.exists(str(path2+img_name)):
            img_name = 'profile_pic.png'
        context['image'] = img_name
        # print('++++++++++++++',img_name)
        if len(feedback_list)!=0:
            context['feedbacks'] = feedback_list
        return render(request,'home/home_student.html',context)
    else:
        feedback_list_group_wise  = dict()
        courses_taught = str(request.user.if_faculty_courses_taught).split(' ')
        for i in courses_taught:
            feedback = Feedback.objects.filter(course_code = i)
            for itr in feedback:
                sid_obj = SentimentIntensityAnalyzer()
                sentiment_dict = sid_obj.polarity_scores(itr.comment)
                star  =  0.0
                if sentiment_dict['compound'] >= 0.75:
                    star = star+ 5
                elif sentiment_dict['compound']>=0.20:
                    star = star+4
                elif sentiment_dict['compound']>= -0.10:
                    star = star+3
                elif sentiment_dict['compound'] >= -0.75:
                    star = star+2
                else:
                    star = star +1
                star= round((star + (itr.que1+itr.que2+itr.que3+itr.que4+itr.que5)/5)/2)
                star_string= str()
                for i in range(star):
                    star_string = star_string+ '+fa fa-star checked'
                for i in range(5-star):
                    star_string = star_string + '+fa fa-star'
                star_string = star_string.split('+')
                feedback_list_group_wise[itr] = (star_string,str(itr))


        img_name = request.user.email
        img_name = img_name.replace('@','')+'.png'
        path2 = settings.MEDIA_ROOT+'\\profile_pic\\'
        if not path.exists(str(path2+img_name)):
            img_name = 'profile_pic.png'
        context['image'] = img_name
        context['feedbacks'] = feedback_list_group_wise
        return render(request,'home/home.html',context)
@login_required(login_url = reverse_lazy('login'))#,kwargs= {'not_logged_in':'You need to login first to access dashboard'}))
def feedback_form(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        print(request.POST.get('course_code'))
        profile = UserProfile.objects.get(user = request.user)
        feedback = form.save(commit = False)
        feedback.user = request.user
        feedback.course_code = request.POST.get('course_code') or 'Hello'
        profile.feedback_filled = profile.feedback_filled+ (' '+request.POST.get('course_code'))
        form.save()
        profile.save()
        return redirect('home:homepage')
    else:
        course_code = request.POST.get('course_code')
        print(request.POST.get('course_code'))
        print("Hell")
        return render(request,'home/feedback_form.html',{'form':form,'course_code':course_code})
def feedback_form_display(request):
    data = str(request.POST.get('form_data')).split(' ')
    print(data[0])
    data_dict = dict()
    data_dict['course_code'] = data[0]
    user = User.objects.get(email = data[3])
    feedback_data = Feedback.objects.filter(user  = user).get(course_code = data[0])
    data_dict['que1'] = feedback_data.que1
    data_dict['que2'] = feedback_data.que2
    data_dict['que3'] = feedback_data.que3
    data_dict['que4'] = feedback_data.que4
    data_dict['que5'] = feedback_data.que5
    data_dict['comment'] = feedback_data.comment
    values_list = {1:'Very Bad',2:'Bad',3:'Neutral',4:'Good',5:'Very Good'}
    data_dict['val'] = values_list
    # f = Feedback.objects.get(user = data[1])
    return render(request,'home/feedback_form.html',data_dict)
