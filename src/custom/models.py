from django.db import models

class Category(models.Model):
    "Product Category"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title




class Product(models.Model):
    "Product Model"
    title = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category, null=False, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
