from django.db import models

# Create your models here.
class UserProfile(models.Model):
    profile_picture = models.FileField(upload_to='profile_pictures', blank=True, null=True)
 

  