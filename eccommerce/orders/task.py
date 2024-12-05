# orders/tasks.py
from celery import shared_task
import time
from .models import Order
from celery.exceptions import Retry

@shared_task(bind=True, max_retries=3)
def process_order(self, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.status = 'processing'
        order.save()
        
        # Sipariş işleme simülasyonu
        # Gerçek dünyada time.sleep yerine bir üçüncü taraf API çağrısı veya başka bir işleme süreci gerçekleşecektir.
        time.sleep(10)
        
        order.status = 'completed'
        order.save()
        return f"Sipariş {order_id} başarıyla tamamlandı"
    
    except Order.DoesNotExist:
        return f"Sipariş {order_id} bulunamadı."
    
    except Exception as e:
        # Görevi yeniden dene
        raise self.retry(exc=e, countdown=5)
