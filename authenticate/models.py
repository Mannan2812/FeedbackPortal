from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import os
from datetime import date
from django.utils import timezone
from django_resized import ResizedImageField
from django.contrib.auth import get_user_model
BRANCH_CHOICES = (
('Select your Branch',
(("CSE","CSE"),
("MECH","MECH"),
("PROD","PROD"),
("CIVIL","CIVIL"),
("AERO","AERO"),
("ECE","ECE"),
("ELEC","ELEC"),
("META","META"))),)
class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser,branch,category,if_faculty_courses_taught, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        branch = branch,
        category = category,
        if_faculty_courses_taught = if_faculty_courses_taught,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password,branch,category,if_faculty_courses_taught, **extra_fields):
    return self._create_user(email, password, False, False,branch,category,if_faculty_courses_taught, **extra_fields)

  def create_superuser(self, email, password,branch,category,if_faculty_courses_taught,**extra_fields):
    user=self._create_user(email, password, True, True,branch,category, if_faculty_courses_taught,**extra_fields)
    return user
CHOICE = (("Faculty","Faculty"),("Student","Student"))

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True,default ="")
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=10,default = "Student",choices = CHOICE)
    branch = models.CharField(max_length = 50,default = "CSE",choices= BRANCH_CHOICES)
    group = models.CharField(max_length = 10,choices = CHOICE)
    if_faculty_courses_taught =models.CharField(max_length = 300,default = '')
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


SEMESTER_COURSES = {
'CSE1':('11A','11B','11C', '11D'),
'CSE2':('11A','11B','11C', '11D'),
'CSE3':('11A','11B','11C', '11D','11E'),
'CSE4':('11A','11B','11C', '11D'),
'CSE5':('11A','11B','11C', '11D'),
'CSE6':('11A','11B','11C', '11D'),
'CSE7':('11A','11B','11C', '11D'),
'CSE8':('11A','11B','11C', '11D'),
'ECE1':('11A','11B','11C', '11D'),
'ECE2':('11A','11B','11C', '11D'),
'ECE3':('11A','11B','11C', '11D'),
'ECE4':('11A','11B','11C', '11D'),
'ECE5':('11A','11B','11C', '11D'),
'ECE6':('11A','11B','11C', '11D'),
'ECE7':('11A','11B','11C', '11D'),
'ECE8':('11A','11B','11C', '11D'),
}
def upload_to_rename(instance,filename):
    ext = filename.split('.')[-1]
    filename ="%s.%s"%(instance.user.email,'png')
    print('++++++++++++',filename)
    return os.path.join('profile_pic',filename)
class UserProfile(models.Model):
    name = models.CharField(max_length = 100,default = "",null = False,blank = False)
    user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    year = models.CharField(max_length =30,default = "1")
    profile_pic = ResizedImageField(size= [233,216],blank = True,null = True,upload_to = upload_to_rename,default = "/media/profile_pic/profile_pic.png")
    branch = models.CharField(max_length = 50,default = "To be updated ")
    CG = models.FloatField(blank = True,null = True)
    Attendance = models.FloatField(blank = True,null =True)
    feedback_filled= models.CharField(max_length = 300,default = ' ',)
    def __str__(self):
        return self.user.email

class Feedback(models.Model):
    course_code = models.CharField(max_length=10,default = '')
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    comment = models.CharField(max_length = 300)
    que1 = models.IntegerField(default = 5)
    que2 = models.IntegerField(default = 5)
    que3 = models.IntegerField(default = 5)
    que4 = models.IntegerField(default = 5)
    que5 = models.IntegerField(default = 5)
        # readonly_fields = ("comment",)
    def __str__(self):
        return self.course_code+'   '+self.user.email








class FeedbackTile(models.Model):
    course_code = models.CharField(max_length=10,default = '')
    course_title = models.CharField(max_length = 10,default = '')
    due_date = models.DateField(null = False,blank = False,default = date.today())
    user_faculty = models.ForeignKey(User,on_delete = models.CASCADE)
    def __str__(self):
        return self.course_code
