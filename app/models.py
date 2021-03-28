from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=500, default='', blank=True)
   link = models.URLField(max_length=128, unique=True, blank=True)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   date_posted = models.DateTimeField(default=timezone.now)


   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
      return reverse('post-detail', kwargs={'pk': self.pk})

   class Meta:
      db_table = ''
      managed = True
      verbose_name = 'Post'
      verbose_name_plural = 'Posts'

