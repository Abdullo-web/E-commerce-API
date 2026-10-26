from django.shortcuts import render
from .models import Order, OrderItem
from .serializers import OrderSerializer
from korzina.models import Korzina, KorzinaUpr
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED

class OrderView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


    def post(self, request):
        basket = get_object_or_404(Korzina, user=request.user)
        items = KorzinaUpr.objects.filter(korzina=basket)

        if not items.exists():
            return Response({'error': 'Korzina Pustoy'},status=HTTP_400_BAD_REQUEST)

        total = 0

        for item in items:
            total += item.product.price * item.quantity

        order = Order.objects.create(user=request.user,total_price=total)

        for item in items:
            OrderItem.objects.create(order=order,product=item.product,quantity=item.quantity,price=item.product.price)

            item.product.kolichestvo -= item.quantity
            item.product.save()

        items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=HTTP_201_CREATED)





class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, order_id):
        order = get_object_or_404(Order,id=order_id,user=request.user)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    def patch(self, request, order_id):
        order = get_object_or_404(Order,id=order_id,user=request.user)

        if order.status != 'pending':
            return Response({'error': 'Mojno otmenit tolko novye zakas'},status=HTTP_400_BAD_REQUEST)

        order.status = 'cancelled'
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    
    


class AdminOrderStatusView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)

        new_status = request.data.get('status')

        if new_status not in [
            'pending',
            'processing',
            'completed',
            'cancelled'
        ]:
            return Response({'error': 'Nepravilny status'},status=HTTP_400_BAD_REQUEST)

        order.status = new_status
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)

