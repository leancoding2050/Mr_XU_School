from django.db import models

# Create your models here.
class SchoolYear(models.Model):
    school_year = models.CharField(max_length=30, verbose_name="年份")

    def __str__(self):
        return f"{ self.school_year }"
    
    class Meta:
        verbose_name = "年份"
        verbose_name_plural = "年份"

class SchoolQuarter(models.Model):
    school_quarter = models.CharField(max_length=30, verbose_name="季度")

    def __str__(self):
        return f"{ self.school_quarter }"
    
    class Meta:
        verbose_name = "季度"
        verbose_name_plural = "季度"
    
class SchoolLanguage(models.Model):
    school_language = models.CharField(max_length=30, verbose_name="語言")

    def __str__(self):
        return f"{ self.school_language }"
    
    class Meta:
        verbose_name = "語言"
        verbose_name_plural = "語言"
    
class SchoolSubject(models.Model):
    school_subject = models.CharField(max_length=30, verbose_name="科目")

    def __str__(self):
        return f"{ self.school_subject }"
    
    class Meta:
        verbose_name = "科目"
        verbose_name_plural = "科目"   
    
class SchoolGrade(models.Model):
    school_grade = models.IntegerField(verbose_name="年級")

    def __str__(self):
        return f"{ self.school_grade }"
    
    class Meta:
        verbose_name = "年級"
        verbose_name_plural = "年級"  
    

class SchoolPrice(models.Model):
    primary_school_price = models.FloatField(default=0, verbose_name="小學價錢")
    middle_school_price = models.FloatField(default=0, verbose_name="初中價錢")
    hight_school_price = models.FloatField(default=0, verbose_name="高中價錢")

    def __str__(self):
        return f"小學：${ self.primary_school_price }, 初中：${ self.middle_school_price }, 高中:${ self.hight_school_price } "
    class Meta:
        verbose_name = "價錢"
        verbose_name_plural = "價錢" 