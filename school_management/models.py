from django.db import models

# Create your models here.
from users.models import User


class Role(models.Model):
    name = models.CharField(max_length=20)  # Diretor, Coordenador, Secretário


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    is_staff = models.BooleanField(default=True)


class SchoolAddress(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)


class School(models.Model):
    name = models.CharField(max_length=80)
    school_address = models.ForeignKey(
        SchoolAddress, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20)
