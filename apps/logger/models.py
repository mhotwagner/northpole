from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

from apps.ornaments.models import OrnamentDevice


class Log(TimeStampedModel):
    ornament = models.ForeignKey(OrnamentDevice, null=False, related_name="logs", on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f'<Log:{self.ornament.nickname or self.ornament.mac_address}>'
