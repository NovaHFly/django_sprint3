from django.contrib.auth import get_user_model
from django.db import models

from core.models import (
    DateCreatedModel,
    PublishedModel,
)

User = get_user_model()


class Category(PublishedModel, DateCreatedModel):
    """Category of posts by the same theme.

    Attributes:
        title (CharField[256]): name of the category.
        slug (SlugField): slug of the category.
        description (TextField): verbose description of the category.
    """

    title = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
    )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Location(PublishedModel, DateCreatedModel):
    """Some landmark.

    Attributes:
        name (CharField[256]): name of the landmark.
    """

    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self) -> str:
        return self.name


class Post(PublishedModel, DateCreatedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        verbose_name='Содержание',
    )
    pub_date = models.DateTimeField(verbose_name='Дата')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Локация',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self) -> str:
        return f'{self.pub_date} - {self.title}'
