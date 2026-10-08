from django.db import models
import random


class Customer(models.Model):

    customer_id = models.PositiveIntegerField(
        unique=True,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    address = models.CharField(max_length=200)

    vehicle_number = models.CharField(
        max_length=20,
        unique=True
    )

    vehicle_model = models.CharField(max_length=100)

    vehicle_type = models.CharField(max_length=50)

    vehicle_image = models.ImageField(
        upload_to='vehicle_images/',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        if not self.customer_id:

            while True:

                new_id = random.randint(10000, 99999)

                if not Customer.objects.filter(
                    customer_id=new_id
                ).exists():

                    self.customer_id = new_id
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name