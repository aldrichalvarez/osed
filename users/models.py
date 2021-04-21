from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   INSTRUCTOR = 'I'
   NOT = 'N'
   PRIVILEGES_CHOICES = [
      (INSTRUCTOR, 'Instructor'),
      (NOT, 'Not'),
   ]
   status = models.CharField(
      max_length=1,
      choices=PRIVILEGES_CHOICES,
      default=NOT,
   )
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   calendar = models.URLField(max_length=128, default='Paste here your Google Calendar shareable link..', blank=True)
   bio = models.CharField(max_length=500, default='Update your profile to add more details about yourself', blank=True)
   address = models.CharField(max_length=500, default='Where are you currently based..', blank=True)
   topics = models.CharField(max_length=500, default='What are the topics you like to talk about..', blank=True)
   education = models.CharField(max_length=500, default='What is your educational background..', blank=True)
   background = models.CharField(max_length=500, default='What is your professional background..', blank=True)
   image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')
   cover = models.ImageField(default='default_cover.png', upload_to='cover_pics')

   def __str__(self):
      return f'{self.user.username} Profile'

   def save(self, *args, **kwargs):
      super(Profile, self).save(*args, **kwargs)
      img = Image.open(self.image.path)
      
      if img.height > 300 or img.width > 300:
         output_size = (300,300)
         img.thumbnail(output_size)
         img.save(self.image.path)
