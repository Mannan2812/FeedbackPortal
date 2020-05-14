
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User,UserProfile,Feedback,FeedbackTile

class UserAdmin(BaseUserAdmin):
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login','branch','category','if_faculty_courses_taught')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2','branch','category','if_faculty_courses_taught')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login','date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# class FeedbackAdmin(admin.ModelAdmin):
#     readonly_fields = ('comment',)
#
#     def address_report(self, instance):
#         # assuming get_full_address() returns a list of strings
#         # for each line of the address and you want to separate each
#         # line by a linebreak
#         return format_html_join(
#             mark_safe('<br>'),
#             '{}',
#             ((line,) for line in instance.get_full_address()),
#         ) or mark_safe("<span class='errors'>I can't determine this address.</span>")
#
#     # short_description functions like a model field's verbose_name
#     address_report.short_description = "Address"




admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Feedback)
admin.site.register(FeedbackTile)
