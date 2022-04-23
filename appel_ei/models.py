from django.db import models

# Create your models here.
class Images(models.Model):
    image= models.ImageField()
    date_added= models.DateTimeField(auto_now_add=True)