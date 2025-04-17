from django.contrib import admin

# Register your models here.

from .models import SchoolBranch ,SchoolBranchArea

admin.site.register(SchoolBranch)
admin.site.register(SchoolBranchArea)