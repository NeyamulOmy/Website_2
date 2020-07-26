from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.TextField(max_length=20)
    pub_date = models.DateField()
    body = models.TextField(max_length=2055)
    image = models.ImageField(upload_to='image/')