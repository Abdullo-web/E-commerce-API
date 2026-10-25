from rest_framework import serializers
from .models import Category,Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
    
class ProductSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )
    class Meta:
        model = Product
        fields = ['id','title','description','price','kolichestvo','category','category_name']