from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, ProductView

router = DefaultRouter()

router.register('categories', CategoryView, basename='categories')
router.register('products', ProductView, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
