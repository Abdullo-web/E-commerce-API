from django.urls import path
from .views import KorzinaView

urlpatterns = [
    path('', KorzinaView.as_view()),
]