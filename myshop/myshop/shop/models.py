from django.db import models
from django.urls import reverse

from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    # _name = models.CharField(max_length=200, db_index=True)
    # _slug = models.SlugField(max_length=200, db_index=True, unique=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, db_index=True, unique=True)
    )

    class Meta:
        # ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(TranslatableModel):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # _name = models.CharField(max_length=200, db_index=True)
    # _slug = models.SlugField(max_length=200, db_index=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, db_index=True),
        description=models.TextField(blank=True)
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # _description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        # index_together = ['id', 'slug']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def quantity(self):
        return [(i, str(i)) for i in range(1, self.stock + 1)]
