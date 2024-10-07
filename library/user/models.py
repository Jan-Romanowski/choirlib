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
    voice_type = models.CharField(max_length=10, default='guest')
    last_activity = models.DateTimeField(null=True, blank=True)
    
    #Это поле используется для определения, имеет ли пользователь доступ к админ-панели Django (/admin). 
    # Если значение is_staff установлено в True, пользователь сможет войти в админ-панель (если у него есть доступ).
    is_staff = models.BooleanField(default=False)

    # Поле Active определяет, активен ли пользователь. Если значение is_active установлено в False, 
    # пользователь не сможет войти в систему, даже если его учетные данные верны.
    is_active = models.BooleanField(default=True)    
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.email