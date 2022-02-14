import uuid

from django.db import models


class Mapping(models.Model):
    path = models.CharField(primary_key=True, max_length=32, editable=False)
    url = models.URLField(max_length=512)
