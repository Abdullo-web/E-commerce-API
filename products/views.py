from django.shortcuts import render
from .models import Category,Product
from .serializers import CategorySerializers,ProductSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions  import IsAdminUser
from .permissions import IsAdminOrReadOnly
from rest_framework.filters import SearchFilter
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



class CategoryView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
    
class ProductView(ModelViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    filter_backends = [SearchFilter]
    search_fields = ['title']
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'category',
                openapi.IN_QUERY,
                description='ID категории',
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'price_min',
                openapi.IN_QUERY,
                description='Минимальная цена',
                type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                'price_max',
                openapi.IN_QUERY,
                description='Максимальная цена',
                type=openapi.TYPE_NUMBER
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        products = Product.objects.all()

        category = self.request.query_params.get('category')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')

        if category:
            products = products.filter(category_id=category)

        if price_min:
            products = products.filter(price__gte=price_min)

        if price_max:
            products = products.filter(price__lte=price_max)

        return products

    
    