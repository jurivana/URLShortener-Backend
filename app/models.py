from django.db import models


class Mapping(models.Model):
    url = models.URLField(max_length=512)
    path = models.CharField(primary_key=True, max_length=32, editable=False)
