from django.db import models

# Create your models here.

class UserRole(models.Model):
    user_role = models.CharField(verbose_name="權限")

    def __str__(self):
        return f"{ self.user_role }"
    
    class Meta:
        verbose_name = "權限"
        verbose_name_plural = "權限"