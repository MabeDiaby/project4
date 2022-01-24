from django.db import models
from datetime import datetime


# https://www.geeksforgeeks.org/urlfield-django-models/
# https://stackoverflow.com/questions/45994290/how-to-make-a-model-field-as-hyperlink-in-django-models
# https://stackoverflow.com/questions/49782499/how-to-add-icons-in-django-forms

# Create your models here.

class Tag(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

# not sure if i should just keep it in profile or make a whole class for it this is mainly for stretch goals


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    timestamp= models.DateTimeField(null=True, blank=True, default=datetime.now())
    # tags = models.ManyToManyField(Tag, null=True, blank=True)
    match= models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post')
    intro=models.CharField(max_length=200) 
    language = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    image_url = models.URLField(max_length=400, null=True, blank=True)
    resume =  models.URLField(max_length=400, null=True, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    stack = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length= 400, null=True, blank=True)
    livelink = models.CharField(max_length=400)
    gitlink = models.CharField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='projects')
    
class Socials(models.Model):
    name= models.CharField(max_length=200)
    image_url = models.CharField(max_length=400,null=True, blank=True)
    link = models.URLField(("Website Link"), max_length=400, db_index=True, unique=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='socials', default="1")