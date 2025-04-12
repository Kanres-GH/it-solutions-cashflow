from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        unique_together = ['name', 'type']

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ['name', 'category']

    def __str__(self):
        return self.name

class CashFlow(models.Model):
    created_at = models.DateField(default=date.today)  # Устанавливаем текущую дату по умолчанию
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)

    def clean(self):
        if self.subcategory.category != self.category:
            raise ValidationError("Подкатегория не соответствует категории.")
        if self.category.type != self.type:
            raise ValidationError("Категория не соответствует типу.")

    def __str__(self):
        return f"{self.created_at} - {self.amount} руб."