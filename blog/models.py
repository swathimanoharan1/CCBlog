# importing django models and users
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
	(0,"Draft"),
	(1,"Publish"),
	(2, "Delete")
)

# creating an django model class

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=300, unique=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	updated_on = models.DateTimeField(auto_now= True)
	created_on = models.DateTimeField()
	content = RichTextUploadingField()
	metades = models.CharField(max_length=200, default="new post")
	status = models.IntegerField(choices=STATUS, default=0)
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	# meta for the class
	class Meta:
		ordering = ['-created_on']
	# used while managing models from terminal
	def __str__(self):
		return self.title
	
class Contact(models.Model):
	name = models.CharField(max_length=100, null=True)
	email = models.EmailField(null=True)
	message = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.email
