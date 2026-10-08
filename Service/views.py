
from django.shortcuts import render, redirect, get_object_or_404

from .models import ServiceBooking
from Accounts.models import Customer


def booking_list(request):

    bookings = ServiceBooking.objects.all()

    return render(
        request,
        'booking_list.html',
        {'bookings': bookings}
    )


def booking_add(request):

    customers = Customer.objects.all()

    if request.method == 'POST':

        ServiceBooking.objects.create(
            customer_id=request.POST.get('customer'),
            booking_date=request.POST.get('booking_date'),
            service_type=request.POST.get('service_type'),
            status=request.POST.get('status'),
            description=request.POST.get('description'),
            service_cost=request.POST.get('service_cost')
        )

        return redirect('booking_list')

    return render(
        request,
        'booking_form.html',
        {'customers': customers}
    )


def booking_update(request, id):

    booking = get_object_or_404(
        ServiceBooking,
        id=id
    )

    customers = Customer.objects.all()

    if request.method == 'POST':

        booking.customer_id = request.POST.get('customer')
        booking.booking_date = request.POST.get('booking_date')
        booking.service_type = request.POST.get('service_type')
        booking.status = request.POST.get('status')
        booking.description = request.POST.get('description')
        booking.service_cost = request.POST.get('service_cost')

        booking.save()

        return redirect(
            'booking_detail',
            booking_id=booking.id
        )

    return render(
        request,
        'booking_update.html',
        {
            'booking': booking,
            'customers': customers
        }
    )


def booking_detail(request, booking_id):

    booking = get_object_or_404(
        ServiceBooking,
        id=booking_id
    )

    return render(
        request,
        'booking_detail.html',
        {
            'booking': booking
        }
    )


def booking_delete(request, id):

    booking = get_object_or_404(
        ServiceBooking,
        id=id
    )

    booking.delete()

    return redirect('booking_list')


def service_history(request):

    bookings = ServiceBooking.objects.filter(
        status='Delivered'
    ).order_by('-booking_date')

    return render(
        request,
        'service_history.html',
        {'bookings': bookings}
    )
