from django.urls import path
from .views import KorzinaView,KorzinaItemView

urlpatterns = [
    path('', KorzinaView.as_view()),
    path('items/<int:item_id>/',KorzinaItemView.as_view()),
]