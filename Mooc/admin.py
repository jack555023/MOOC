from django.contrib import admin
from courses.models import Courselist
from users.models import Webuser


class WebUserAdmin(admin.ModelAdmin):
    list_display = ('useremail', 'user_password')


class CourselistAdmin(admin.ModelAdmin):
    list_display = ('webuser','coursedbname','coursename') 


admin.site.register(Courselist,CourselistAdmin)
admin.site.register(Webuser,WebUserAdmin)
