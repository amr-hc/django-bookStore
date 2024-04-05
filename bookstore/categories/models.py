from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def delete_url(self):
        return reverse('categories.delete', args=[self.id])

    @property
    def edit_url(self):
        return reverse('categories.edit', args=[self.id])

    @property
    def detail_url(self):
        return reverse('categories.detail', args=[self.id])
