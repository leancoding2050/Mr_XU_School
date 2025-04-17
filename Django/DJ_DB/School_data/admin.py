from django.contrib import admin

# Register your models here.

from .models import SchoolYear, SchoolQuarter , SchoolLanguage, SchoolPrice, SchoolGrade ,SchoolSubject

admin.site.register(SchoolYear)
admin.site.register(SchoolQuarter)
admin.site.register(SchoolLanguage)
admin.site.register(SchoolPrice)
admin.site.register(SchoolGrade)
admin.site.register(SchoolSubject)