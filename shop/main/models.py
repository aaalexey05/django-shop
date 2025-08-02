from django.db import models
from django.template.base import kwarg_re
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    # Product 1
    # domen.com/products/product-1 -> slug 
    # CEO 

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # related_name - имя, по которому мы можем обратиться к продуктам из категории
    # on_delete - что делать с продуктами при удалении категории
    # CASCADE - удаляем все продукты при удалении категории
    # PROTECT - запрещаем удаление категории, если есть продукты в ней
    # SET_NULL - устанавливаем null в поле category
    # SET_DEFAULT - устанавливаем default значение в поле category
    # DO_NOTHING - ничего не делаем
    
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name    

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])  # type: ignore