from rest_framework import serializers
from .models import Korzina, KorzinaUpr


class KorzinaUprSerializers(serializers.ModelSerializer):
    class Meta:
        model = KorzinaUpr
        fields = ['id', 'product', 'quantity']


class KorzinaSerializers(serializers.ModelSerializer):
    items = KorzinaUprSerializers(many=True, read_only=True)

    class Meta:
        model = Korzina
        fields = ['id', 'items']