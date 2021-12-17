from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Plants(models.Model):
    name = models.CharField(max_length=200, null=True)
    bioactive_compound = models.CharField(max_length=200, null=True)
    uses = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Scrape(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=2080)

    def __str__(self):
        return self.name
