from os import name
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import SlugField
from .manager import ServiceQuerySet
from .fileupload import services_path
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = SlugField(null=True, blank=True, default=None, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Services(models.Model):
    title = models.CharField(max_length=225)
    slug = SlugField(null=True, blank=True, default=None, unique=True)
    icons = models.CharField(max_length=20, null=True, blank=True)
    timeline = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to=services_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    objects = models.Manager()
    status_objects = ServiceQuerySet()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Services, self).save(*args, **kwargs)
        # img = Image.open(self.image.path)

        # if img.height > 420 or img.width > 700:
        #     output_size = (420, 700)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service-detail-page', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=30)
    find_us = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
