# ecommerce/urls.py
from django.urls import path
from orders.views import OrderCreateView, OrderListView, OrderStatusView

app_name = 'orders' 

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create_order'),
    path('status/', OrderStatusView.as_view(), name='order_status'),
    path('list/', OrderListView.as_view(), name='list'),
]