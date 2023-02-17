import uuid

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    category = models.ForeignKey(
        "taxonomies.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="articles",
    )
    tags = models.ManyToManyField("taxonomies.Tag", related_name="articles")
