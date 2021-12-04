from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug=models.SlugField(default="",blank=True,max_length=50)
    auther=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated=models.DateTimeField(auto_now=True,blank=True,null=True)
# localhost:8000/blog/slug-text
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("blog:detail", args=[str(self.slug)])
    