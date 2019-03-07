from django.db import models


# Create your models here.

class ContactForm(models.Model):

    Name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
