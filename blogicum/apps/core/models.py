from django.db import models


# Create your models here.
class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано'
    )

    class Meta:
        abstract = True


class DateCreatedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Добавлено'
    )

    class Meta:
        abstract = True
