from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    numberOfPages = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/images')

    def __str__(self):
        return self.title

    @property
    def book_url(self):
        return reverse('detailsDB',args=[self.id])

    @property
    def image_url(self):
        return f"/media/{self.image}"

    @property
    def update_url(self):
        return reverse('updateBook',args=[self.id])
