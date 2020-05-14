from django.urls import path,include
from .views import HomePage,feedback_form,feedback_form_display
from authenticate.views import login_user,logout_user,edit_profile

app_name = "home"
urlpatterns = [
path('',HomePage,name = 'homepage'),
path('str<str:message>/',HomePage,name = 'homepage2'),
# path('logout/',logout_user,name= 'logout'),
path('feedback/',feedback_form,name = 'feedback_form'),
# path('profile/',edit_profile,name = 'edit_profile'),
path('feedback_display',feedback_form_display,name = 'feedback_form_display'),
]
