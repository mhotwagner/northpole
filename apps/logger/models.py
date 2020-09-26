from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Log(TimeStampedModel):
    message = models.TextField()