from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from students.models import Subject

# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=20)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.ForeignKey(
        Gender, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def has_perm(self, perm, object=None):
        return True

    def has_module_perms(self, app_Label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True)
