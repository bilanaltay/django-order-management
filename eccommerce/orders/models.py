from django.db import models

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Beklemede'),
        ('processing', 'İşleniyor'),
        ('completed', 'Tamamlandı'),
    )
    
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()  # Ensure quantity is a positive IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        """Returns a string representation of the Order instance, displaying the product name, quantity, and human-readable status. """
        return f"Order({self.product_name}, Qty: {self.quantity}, Status: {self.get_status_display()})"
