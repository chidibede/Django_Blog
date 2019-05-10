from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	website = models.CharField(max_length=200, null=True, blank=True)


	def __str__(self):
		return self.user.username + ' profile'


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 150 or img.width > 150:
			output_size = (150, 150)
			img.thumbnail(output_size)
			img.save(self.image.path)
