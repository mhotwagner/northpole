from django.db import models

from django_extensions.db.models import TimeStampedModel


class OrnamentDevice(TimeStampedModel):
    mac_address = models.CharField(db_index=True, max_length=12)

    def __str__(self):
        return f'Ornament<{self.mac_address}>'
