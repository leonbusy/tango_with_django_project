from pyexpat import model
from django import views
from django.db import models
#need to add slugify module
#from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)

    #chapter6 code
    #slug = models.SlugField(blank=True)
    slug=models.SlugField(unique=True)
    #slug=models.SlugField(blank=True,unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Page(models.Model):
    #add category title url and views in class page 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title

# class Category(models.Model):
#     name = models.CharField(max_length=128, unique=True)

#     class Meta:
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username