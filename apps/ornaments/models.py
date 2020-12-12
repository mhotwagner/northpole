from django.db import models

from django_extensions.db.models import TimeStampedModel


class OrnamentDevice(TimeStampedModel):
    mac_address = models.CharField(db_index=True, max_length=12)
    nickname = models.CharField(max_length=64, unique=True, null=True)

    def __str__(self):
        if self.nickname:
            return f'Ornament<{self.nickname}:{self.mac_address}>'
        return f'Ornament<{self.mac_address}>'

    def save(self, **kwargs):
        if ':' in self.mac_address:
            self.mac_address = self.mac_address.replace(':', '')
        super(OrnamentDevice, self).save(**kwargs)
