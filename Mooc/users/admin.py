from django.contrib import admin
from courses.models import Courselist
from users.models import Webuser


class WebUserAdmin(admin.ModelAdmin):
		model = Webuser
		list_display = ('useremail', 'user_password','isvalid','valid_code')
		list_filter = ['useremail']

admin.site.register(Webuser,WebUserAdmin)
