from rest_framework import serializers

from apps.ornaments.models import OrnamentDevice


class OrnamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrnamentDevice
        # TODO: Fix this shit up
        fields = '__all__'
