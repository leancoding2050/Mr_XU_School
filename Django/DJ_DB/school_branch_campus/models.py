from django.db import models

# Create your models here.

class SchoolBranch(models.Model):
    school_branch = models.CharField(max_length=30, verbose_name="分校")

    def __str__(self):
        return f"{self.school_branch}"
    
    class Meta:
        verbose_name = "分校"
        verbose_name_plural = "分校"    

    
class SchoolBranchArea(models.Model):
    school_branch_Area = models.CharField(max_length=30, verbose_name="分校地區")

    def __str__(self):
        return f"{self.school_branch_Area}"
    
    class Meta:
        verbose_name = "分校地區"
        verbose_name_plural = "分校地區"    