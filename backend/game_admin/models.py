from django.db import models
from django.db.models.functions import Now

# Create your models here.
class Contact(models.Model):
    fullName = models.CharField(max_length = 250, blank=False, null = False)
    email= models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created = models.DateTimeField(db_default=Now())

    def __str__(self):
        return self.fullName

class Category(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='games')
    image = models.ImageField(upload_to="game_images/", blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.title
