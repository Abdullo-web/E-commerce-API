from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Korzina, KorzinaUpr
from .serializers import KorzinaSerializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi





class KorzinaView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    
    def get(self,request):
        korzina, create = Korzina.objects.get_or_create(user = request.user)
        serializer = KorzinaSerializers(korzina)
        return Response(serializer.data)
    
    @swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'product': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description='ID товара'
            ),
            'quantity': openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description='Количество товара'
            ),
        },
        required=['product']
    )
)
    
    def post(self,request):
        korzina, created = Korzina.objects.get_or_create(user=request.user)
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        
        try:
            quantity = int(quantity)
            
        except (TypeError, ValueError):
            return Response(
                {'error': 'Количество должно быть целым числом'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if quantity < 1:
            return Response(
                {'error': 'Количество должно быть больше 0'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            item = KorzinaUpr.objects.get(korzina=korzina, product_id=product_id)
            item.quantity += quantity
            item.save()
            
        except KorzinaUpr.DoesNotExist:
            item = KorzinaUpr.objects.create(korzina=korzina,product_id=product_id,quantity=quantity)
            
        except (TypeError, ValueError):
            return Response(
                {'error': 'Неверный ID товара'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = KorzinaSerializers(korzina)
        return Response(serializer.data, status=status.HTTP_200_OK)