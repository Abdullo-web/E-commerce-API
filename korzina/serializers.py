from rest_framework import serializers
from .models import Korzina, KorzinaUpr


class KorzinaUprSerializers(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title',read_only=True)
    product_price = serializers.DecimalField(source='product.price',max_digits=7,decimal_places=2,read_only=True)
    summa = serializers.SerializerMethodField()
    
    class Meta:
        model = KorzinaUpr
        fields = ['id', 'product','product_title','product_price', 'quantity', 'summa']

    def get_summa(self, obj):
        return obj.product.price * obj.quantity
    
    
class KorzinaSerializers(serializers.ModelSerializer):
    items = KorzinaUprSerializers(many=True, read_only=True)
    obshaya_summa = serializers.SerializerMethodField()

    class Meta:
        model = Korzina
        fields = ['id', 'items','obshaya_summa']
        
    def get_obshaya_summa(self, obj):
        obshaya_summa = 0

        for item in obj.items.all():
            summa_tovara = item.product.price * item.quantity
            obshaya_summa += summa_tovara

        return obshaya_summa