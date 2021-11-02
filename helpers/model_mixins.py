from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify


class TitleMixin(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, blank=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class OrderMixin(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class UserMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GenericModelMixin(models.Model):
    limits = models.Q(app_label='common', model='feedback') | \
             models.Q(app_label='common', model='quote')

    model_type = models.ForeignKey(
        ContentType,
        verbose_name="Content Type",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        limit_choices_to=limits
    )

    model_id = models.PositiveIntegerField('object id', blank=True, null=True)
    model_object = GenericForeignKey('model_type', 'model_id')

    class Meta:
        abstract = True
