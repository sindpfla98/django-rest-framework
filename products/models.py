from django.db import models

# 상품 테이블
class Product(models.Model):
    GENDER_CHOICES = [
        ('all', 'all'),
        ('male', 'male'),
        ('female', 'female')
    ]
    CATEGORY_CHOICES = [
        ('skincare', 'skincare'),
        ('maskpack', 'maskpack'),
        ('suncare', 'suncare'),
        ('basemakeup','basemakeup')
    ]
    imageId = models.TextField()
    name = models.TextField()
    price = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    ingredients = models.TextField()
    monthlySales = models.IntegerField(default=0)
    oily = models.IntegerField(null=True)
    dry = models.IntegerField(null=True)
    sensitive = models.IntegerField(null=True)

# 성분 테이블
class Ingredient(models.Model):
    SKIN_TYPE_CHOICES=[("O", "O"), ("X", "X")]
    name = models.TextField()
    oily = models.CharField(max_length=2, choices=SKIN_TYPE_CHOICES, null=True)
    dry = models.CharField(max_length=2, choices=SKIN_TYPE_CHOICES, null=True)
    sensitive = models.CharField(max_length=2, choices=SKIN_TYPE_CHOICES, null=True)
