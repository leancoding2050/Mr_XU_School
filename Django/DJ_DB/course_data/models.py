from django.db import models

# Create your models here.
class CourseTime(models.Model):
    course_time = models.CharField(max_length=30, verbose_name="時間")

    def __str__(self):
        return f"{ self.course_time }"
     
    class Meta:
        verbose_name = "時間"
        verbose_name_plural = "時間"      


class CourseRoom(models.Model):
    course_room = models.CharField(max_length=30, verbose_name="課室")

    def __str__(self):
        return f"{ self.course_room }"
    class Meta:
        verbose_name = "課室"
        verbose_name_plural = "課室"  

class CourseLevel(models.Model):
    course_level = models.CharField(max_length=30, verbose_name="難度")

    def __str__(self):
        return f"{ self.course_level }"
    
    class Meta:
        verbose_name = "難度"
        verbose_name_plural = "難度"  
    
class CourseLesson(models.Model):
    course_lesson = models.CharField(max_length=30, verbose_name="節數")

    def __str__(self):
        return f"{ self.course_lesson }"
    
    class Meta:
        verbose_name = "節數"
        verbose_name_plural = "節數"  