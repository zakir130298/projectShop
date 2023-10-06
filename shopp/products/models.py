from django.db import models
from django.contrib.auth.models import User

# pip install Pillow
class CategoryModel(models.Model):
    title = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(CategoryModel, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.FileField(upload_to='product')
    favorited_by = models.ManyToManyField(User, related_name='favorite_products', blank=True)
    descriptions = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Добавления продукта'
        verbose_name_plural = 'Добавлаения продуктов'
