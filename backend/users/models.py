from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):

    email = models.EmailField(
        unique=True,
        max_length=254,
        blank=False,
        verbose_name="email"
    )

    first_name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name="Имя"
    )

    last_name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name="Фамилия"
    )

    username = models.CharField(
        unique=True,
        max_length=150,
        blank=False,
        verbose_name="Юзернейм"
    )

    is_subscribed = models.ManyToManyField(
        'User',
        through='Subscription',
        related_name='subscriptions',
        verbose_name='Подписки',
        blank=True
    )

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.username


class Subscription(models.Model):

    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'author'],
                name='user_author_unique'
            )
        ]

    def __str__(self):
        return f'{self.user} подписан  на {self.author}'
