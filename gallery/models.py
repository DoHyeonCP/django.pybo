from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery_images/')