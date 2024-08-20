from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Добавляем это поле
    date_joined = models.DateTimeField(default=timezone.now)

    # Custom fields for roles
    is_admin = models.BooleanField(default=False)
    is_regular_user = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.email
    
    class Meta:
        permissions = [
            ("can_view_files", "Ma dostęp do przeglądania plików"),
            ("can_edit_compositions", "Ma dostęp do edycji utworów"),
            ("can_edit_folders", "Ma dostęp do edycji teczek"),
            ("can_edit_news", "Ma dostęp do edycji aktualności")
        ]
