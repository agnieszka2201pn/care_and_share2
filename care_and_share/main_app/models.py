from django.contrib.auth.models import User
from django.db import models

from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=64)


types = (
    (0, 'Fundacja'),
    (1, 'Organizacja pozarządowa'),
    (2, 'Zbiórka lokalna'),
)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=types, default=0)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.get_type_display()}: {self.name}. Opis: {self.description}'


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.TextField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField(null=True)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

