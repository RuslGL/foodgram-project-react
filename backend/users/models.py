from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.db.models import UniqueConstraint


class User(AbstractUser):

    email = models.EmailField(
        'email',
        unique=True
    )
    
    first_name = models.CharField(
        'Имя',
        max_length=50,
        blank=False
    )
    
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        blank=False)
    
    username = models.CharField(
        'Логин',
        max_length=50,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.username
