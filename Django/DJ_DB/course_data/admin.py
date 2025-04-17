from django.contrib import admin

# Register your models here.

from .models import CourseLesson , CourseLevel , CourseRoom ,CourseTime

admin.site.register(CourseLesson)
admin.site.register(CourseLevel)
admin.site.register(CourseRoom)
admin.site.register(CourseTime)
