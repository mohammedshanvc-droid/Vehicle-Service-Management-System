
from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking_list, name='booking_list'),

    path('bookings/add/', views.booking_add, name='booking_add'),

    path('bookings/update/<int:id>/', views.booking_update, name='booking_update'),

    path('bookings/delete/<int:id>/', views.booking_delete, name='booking_delete'),

    path('history/', views.service_history, name='service_history'),

    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
]

