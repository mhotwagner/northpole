from django.db import models

from django_extensions.db.models import TimeStampedModel


class OrnamentDevice(TimeStampedModel):
    mac_address = models.CharField(db_index=True, max_length=12)
    nickname = models.CharField(max_length=64, unique=True, null=True)

    @property
    def id(self):
        return self.mac_address

    def __str__(self):
        if self.nickname:
            return f'Ornament<{self.nickname}>'
        return f'Ornament<{self.mac_address}>'
