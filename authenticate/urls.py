from django.urls import path,include
from django.shortcuts import redirect
from .views import login_user,register,edit_profile,logout_user
from .forms import CustomPasswordForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
app_name = "authenticate"
urlpatterns = [
path('login/',login_user,name = 'login'),
path('register/',register,name = 'register'),
path('profile/',edit_profile,name = "edit_profile"),
path('logout/',logout_user,name = 'logout'),
path('change-password/',
    auth_views.PasswordChangeView.as_view(template_name='authenticate/change-password.html',
        success_url = reverse_lazy('home:homepage2',kwargs= {"message":'success'}),
        form_class= CustomPasswordForm
    ),
    name='change_password'
),



]
