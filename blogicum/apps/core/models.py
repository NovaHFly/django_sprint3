from django.db import models


# Create your models here.
class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True, verbose_name='Отображается'
    )

    class Meta:
        abstract = True


class DateCreatedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Создано'
    )

    class Meta:
        abstract = True
