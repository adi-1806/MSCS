from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['id']
        verbose_name = "user"
        verbose_name_plural = "users"


class Societies(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    pan = models.CharField(max_length=50)
    tan = models.CharField(max_length=50)
    name_of_md = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    email_id = models.EmailField()
    service_tax_no = models.IntegerField()


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name