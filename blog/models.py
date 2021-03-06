from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):  
    objects = models.Manager()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)


    def __str__(self):
    	return self.username + "'s post"

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})
