from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    description = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    experience = models.FloatField(help_text="Experience in years", default=0)
    salary = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo_urls = models.JSONField(default=list, blank=True)  # list of photo urls
    ratings = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
