from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return f"{self.name}"

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, verbose_name='Kategoria')
    name = models.CharField(max_length=255, verbose_name='Nazwa')
    description = models.TextField(blank=True, null=True, verbose_name='Opis')
    price = models.FloatField(verbose_name='Cena')
    image = models.ImageField(upload_to='item_images', blank=False, null=False, verbose_name='Zdjęcie')
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"