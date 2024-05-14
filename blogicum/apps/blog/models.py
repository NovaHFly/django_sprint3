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
        title (CharField[256]): Name of the category.
        slug (SlugField): Slug of the category.
        description (TextField): Verbose description of the category.
    """

    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        unique=True,
    )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Location(PublishedModel, DateCreatedModel):
    """Some landmark.

    Attributes:
        name (CharField[256]): Name of the landmark.
    """

    name = models.CharField(
        max_length=256,
        verbose_name='Название места',
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self) -> str:
        return self.name


class Post(PublishedModel, DateCreatedModel):
    """A single post.

    Attributes:
        title (CharField[256]): Title of the post.
        text (TextField): Text of the post.
        pub_date (DateTimeField): Date and time when the post was published.
        author (FK[User]): Author of the post.
        location (FK[Location]): Location, connected to the post.
        category (FK[Category]): Category of the post.
    """

    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self) -> str:
        return f'{self.pub_date} - {self.title}'
