from django.urls import path
from .views import OrderView,OrderDetailView,AdminOrderStatusView

urlpatterns = [
    path('', OrderView.as_view()),
    path('<int:order_id>/', OrderDetailView.as_view()),
    path('admin/<int:order_id>/status/',AdminOrderStatusView.as_view()),
]
