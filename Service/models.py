from django.db import models
from Accounts.models import Customer


class ServiceBooking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Service', 'In Service'),
        ('Completed', 'Completed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    booking_date = models.DateField()

    service_type = models.CharField(
        max_length=100
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    description = models.TextField()

    service_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.customer.name