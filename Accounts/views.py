from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import models
from Service.models import ServiceBooking
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def customer_login(request):

    if request.method == 'POST':

        customer_id = request.POST.get('customer_id')

        try:

            customer = Customer.objects.get(
                customer_id=customer_id
            )

            request.session['customer_id'] = customer.customer_id

            return redirect('customer_dashboard')

        except Customer.DoesNotExist:

            return render(
                request,
                'customer_login.html',
                {
                    'error': 'Invalid Customer ID'
                }
            )

    return render(
        request,
        'customer_login.html'
    )


def customer_dashboard(request):

    customer_id = request.session.get('customer_id')

    if not customer_id:
        return redirect('customer_login')

    try:

        customer = Customer.objects.get(
            customer_id=customer_id
        )

    except Customer.DoesNotExist:

        return redirect('customer_login')

    bookings = ServiceBooking.objects.filter(
        customer=customer
    ).order_by('-booking_date')

    return render(
        request,
        'customer_dashboard.html',
        {
            'customer': customer,
            'bookings': bookings
        }
    )


def customer_logout(request):

    request.session.pop(
        'customer_id',
        None
    )

    return redirect('customer_login')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:

            login(request, user)

            return redirect('staff_dashboard')

        else:

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid staff username or password'
                }
            )

    return render(
        request,
        'login.html'
    )


def forgot_password(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        try:

            user = User.objects.get(
                username=username,
                is_staff=True
            )

            request.session['reset_user_id'] = user.id

            return redirect('reset_password')

        except User.DoesNotExist:

            return render(
                request,
                'forgot_password.html',
                {
                    'error': 'Invalid staff username'
                }
            )

    return render(
        request,
        'forgot_password.html'
    )


def reset_password(request):

    user_id = request.session.get('reset_user_id')

    if not user_id:

        return redirect('forgot_password')

    try:

        user = User.objects.get(
            id=user_id,
            is_staff=True
        )

    except User.DoesNotExist:

        request.session.pop(
            'reset_user_id',
            None
        )

        return redirect('forgot_password')

    if request.method == 'POST':

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            return render(
                request,
                'reset_password.html',
                {
                    'error': 'Passwords do not match'
                }
            )

        if len(password) < 8:

            return render(
                request,
                'reset_password.html',
                {
                    'error': 'Password must contain at least 8 characters'
                }
            )

        user.set_password(password)
        user.save()

        request.session.pop(
            'reset_user_id',
            None
        )

        return redirect(
            'password_reset_success'
        )

    return render(
        request,
        'reset_password.html'
    )


def password_reset_success(request):

    return render(
        request,
        'password_reset_success.html'
    )


def staff_dashboard(request):

    return render(
        request,
        'staff_dashboard.html'
    )

def customer_list(request):

    search = request.GET.get('search', '').strip()

    customers = Customer.objects.all()

    if search:

        customers = customers.filter(
            Q(customer_id__icontains=search) |
            Q(name__icontains=search) |
            Q(phone__icontains=search) |
            Q(email__icontains=search) |
            Q(vehicle_number__icontains=search) |
            Q(vehicle_model__icontains=search) |
            Q(vehicle_type__icontains=search)
        )

    return render(
        request,
        'customer_list.html',
        {
            'customers': customers,
            'search': search
        }
    )
def customer_add(request):

    if request.method == 'POST':

        Customer.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            vehicle_number=request.POST.get('vehicle_number'),
            vehicle_model=request.POST.get('vehicle_model'),
            vehicle_type=request.POST.get('vehicle_type'),
            vehicle_image=request.FILES.get('vehicle_image')
        )

        return redirect('customer_list')

    return render(
        request,
        'customer_form.html'
    )


def customer_update(request, id):

    customer = get_object_or_404(
        Customer,
        id=id
    )

    if request.method == 'POST':

        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('phone')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.vehicle_number = request.POST.get('vehicle_number')
        customer.vehicle_model = request.POST.get('vehicle_model')
        customer.vehicle_type = request.POST.get('vehicle_type')

        if request.FILES.get('vehicle_image'):

            customer.vehicle_image = request.FILES.get(
                'vehicle_image'
            )

        customer.save()

        return redirect(
            'customer_list'
        )

    return render(
        request,
        'customer_update.html',
        {
            'customer': customer
        }
    )


def customer_delete(request, id):

    customer = get_object_or_404(
        Customer,
        id=id
    )

    customer.delete()

    return redirect(
        'customer_list'
    )


def user_logout(request):

    logout(request)

    return redirect(
        'user_login'
    )
    
    
    