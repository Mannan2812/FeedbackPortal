from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.contrib.auth.models import User
class UserBackend(ModelBackend):
    def authenticate(self,request,**kwargs):
        email = kwargs['email']
        password = kwargs['password']
        try:
            user_info  =UserProfile.objects.get(email = email)
            if user_info.password==password:
                return user_info
        except UserProfile.DoesNotExist:
            pass
