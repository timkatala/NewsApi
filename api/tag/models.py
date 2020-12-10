from django.db import models
from django.utils.translation import gettext as _


class Tag(models.Model):
    name = models.CharField(max_length=30, null=False)