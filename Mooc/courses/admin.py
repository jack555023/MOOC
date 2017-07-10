from django.contrib import admin
from courses.models import *

class CourselistAdmin(admin.ModelAdmin):
		model = Courselist
		list_display = ('webuser','coursedbname','coursename') 
		list_filter = ['coursename']


class CourseOverviewsAdmin(admin.ModelAdmin):
	model = CourseOverviews
	list_display =  ('course_name','course_code','category','instructor','open_date','close_date','op','ac','platform','update_date','renew','total_visitors','total_enrolled_learners','enroll_learner_rate','active_learners','active_learners_rate','course_completers','course_completer_rate')
	list_filter = ['course_name']


admin.site.register(Courselist,CourselistAdmin)
admin.site.register(CourseOverviews,CourseOverviewsAdmin)
