from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, DetailView, ListView
from .models import Order
from .task import process_order

class OrderCreateView(CreateView):
    model = Order
    template_name = 'orders/create_order.html'
    fields = ['product_name', 'quantity']
    success_url = '/orders/status/'

    def form_valid(self, form): 
        response = super().form_valid(form)
        try:
            task = process_order.delay(self.object.id)
            self.object.task_id = task.id
            self.object.save()
            messages.success(self.request, "Siparişiniz başarıyla oluşturuldu.")
        except Exception as e:
            self.object.delete()  # Siparişi kaydettiyseniz geri alın
            raise RuntimeError("Order processing task failed") from e
        return response

class OrderStatusView(DetailView):
    model = Order
    template_name = 'orders/order_status.html'
    
    def get_object(self):
        return Order.objects.latest('created_at')
    
class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']  # En son siparişler üstte görünsün
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_ordering(self):
        return self.request.GET.get('ordering', '-created_at')
