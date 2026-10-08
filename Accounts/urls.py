from django.urls import path
from . import views

urlpatterns = [

    path(
        'login/',
        views.user_login,
        name='user_login'
    ),

    path(
        'forgot-password/',
        views.forgot_password,
        name='forgot_password'
    ),

    path(
        'reset-password/',
        views.reset_password,
        name='reset_password'
    ),

    path(
        'password-reset-success/',
        views.password_reset_success,
        name='password_reset_success'
    ),

    path(
        'customer-login/',
        views.customer_login,
        name='customer_login'
    ),

    path(
        'staff-dashboard/',
        views.staff_dashboard,
        name='staff_dashboard'
    ),

    path(
        'customer-dashboard/',
        views.customer_dashboard,
        name='customer_dashboard'
    ),

    path(
        'customers/',
        views.customer_list,
        name='customer_list'
    ),

    path(
        'customers/add/',
        views.customer_add,
        name='customer_add'
    ),

    path(
        'customers/update/<int:id>/',
        views.customer_update,
        name='customer_update'
    ),

    path(
        'customers/del/<int:id>/',
        views.customer_delete,
        name='customer_delete'
    ),

    path(
        'customer-logout/',
        views.customer_logout,
        name='customer_logout'
    ),

    path(
        'logout/',
        views.user_logout,
        name='user_logout'
    ),

]