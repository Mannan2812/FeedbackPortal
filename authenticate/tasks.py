from datetime import date,timezone
from authenticate.models import User,UserProfile,FeedbackTile
from django.core.mail import  send_mail
from .models import SEMESTER_COURSES
# import celery
#
# @celery.decorators.periodic_task(run_every  =datetime.timedelta(seconds= 5))
def myTask():
    users = User.objects.filter(category = "Student");
    mail_recepients_list = list()
    for u in users:
        profile = UserProfile.objects.get(user = u)
        code = str(u.branch)+str(profile.year)+'1'
        feedback_filled=  profile.feedback_filled.split(' ')
        for course in SEMESTER_COURSES[code]:
                if course not in feedback_filled:
                    f = FeedbackTile.objects.get(course_code = str(course))
                    if (f.due_data-datetime.now(timezone.utc)).days<=1:
                        if u.email not in mail_recepients_list:
                            mail_recepients_list.append(u.email)
                            break
    send_mail('Feedbacks Pending', 'Please fill your pending feedback by logging into PEC Feedback portal', 'mannanbansal3@gmail.com',mail_recepients_list)
    for ft in FeedbackTile.objects.all():
        if (ft.due_data-datetime.now(timezone.utc)).days<0:
            ft.delete()
