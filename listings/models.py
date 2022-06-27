from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    description = models.CharField(max_length=900)
    address = models.CharField(max_length=100)
    image = CloudinaryField('real estate')

    def __str__(self):
        return self.title