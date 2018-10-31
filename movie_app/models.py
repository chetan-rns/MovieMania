from django.db import models
from slugify import slugify
# Create your models here.

class Users(models.Model):
	name=models.CharField(max_length=250)
	user_name=models.CharField(max_length=250,unique=True)
	password=models.CharField(max_length=250)

	def __str__(self):
		return self.user_name

class Videos(models.Model):
	video_title=models.CharField(max_length=250,unique=True)
	slug = models.SlugField(unique=True)
	video_user=models.ManyToManyField(Users,through="Favourites")
	def save(self, *args, **kwargs):
		self.slug = slugify(self.video_title)
		super(Videos, self).save(*args, **kwargs)
	def __str__(self):
		return self.video_title

class Favourites(models.Model):
	video_title=models.ForeignKey(Videos, on_delete=models.CASCADE)
	user_name=models.ForeignKey(Users, on_delete=models.CASCADE)
	upvotes=models.IntegerField(default=0)
	downvotes=models.IntegerField(default=0)
	fav=models.BooleanField(default=False)	
	class Meta:
		unique_together=('video_title','user_name')			

















