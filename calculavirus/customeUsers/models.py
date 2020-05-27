from django.db import models

# Create your models here.

class CustomUsers(models.Model):
    name = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250)

    def __str__(self):
        return "%s" % self.name
