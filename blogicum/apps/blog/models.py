from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(
        max_length=64,
        verbose_name='Название',
    )
    slug = models.SlugField(
        max_length=64,
        verbose_name='Слаг',
        unique=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class BlogPost(PublishedModel):
    date = models.DateField(verbose_name='Дата публикации')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='posts',
        null=True,
    )
    location = models.CharField(
        max_length=64,
        verbose_name='Локация',
        null=True,
        blank=True,
    )
    text = models.TextField(
        max_length=512,
        verbose_name='Текст публикации',
    )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self) -> str:
        return f'{self.date} - {self.location}'
