from email.mime import image
from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse





# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.description, self.uniqueId)    


    def get_absolute_url(self):
        return reverse('photo', kwargs={'slug': self.slug})
     

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify(self.uniqueId)

        self.slug = slugify(self.uniqueId)
        super(Photo, self).save(*args, **kwargs) 

