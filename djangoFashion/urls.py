"""
URL configuration for djangoFashion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from fashion import views
from fashion.views import afterlogin_view, customer_signup_view, customer_home_view, search_view, admin_products_view, \
    admin_add_product_view, view_customer_view, update_customer_view, delete_customer_view, admin_view_booking_view, \
    delete_product_view, update_product_view, send_feedback_view, view_feedback_view, home_view, add_to_cart_view, \
    customer_address_view, remove_from_cart_view, cart_view, payment_success_view, update_order_view, my_order_view, \
    delete_order_view, adminclick_view, aboutus_view, contactus_view, download_invoice_view, edit_profile_view, \
    my_profile_view, admin_dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/',  afterlogin_view, name='home'),
    path('afterlogin', afterlogin_view, name='afterlogin'),
    path('customersignup', customer_signup_view),
    path('customer-login', LoginView.as_view(template_name='customer_login.html'), name='customer-login'),
    path('admin-dashboard/', TemplateView.as_view(template_name='admin_dashboard.html'), name='admin-dashboard'),
    path('customer-home', customer_home_view, name='customer-home'),
    path('search', search_view, name='search'),
    path('admin-products', admin_products_view, name='admin-products'),
    path('admin-add-product', admin_add_product_view, name='admin-add-product'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'), name='adminlogin'),
    path('view-customer', view_customer_view,name='view-customer'),
    path('update-customer/<int:pk>', update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>', delete_customer_view, name='delete-customer'),
    path('admin-view-booking', admin_view_booking_view,name='admin-view-booking'),
    path('admin-products', admin_products_view,name='admin-products'),
    path('admin-add-product',admin_add_product_view,name='admin-add-product'),
    path('delete-product<int:pk>', delete_product_view, name='delete-product'),
    path('updateproduct/<int:pk>', update_product_view, name='update-product'),
    path('send-feedback', send_feedback_view,name='send-feedback'),
    path('view-feedback', view_feedback_view,name='view-feedback'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('add-to-cart/<int:pk>', add_to_cart_view,name='add-to-cart'),
    path('cart', cart_view, name='cart'),
    path('remove-from-cart/<int:pk>', remove_from_cart_view, name='remove-from-cart'),
    path('customer-address', customer_address_view, name='customer-address'),
    path('payment-success',payment_success_view, name='payment-success'),
    path('delete-order/<int:pk>', delete_order_view, name='delete-order'),
    path('update-order/<int:pk>', update_order_view, name='update-order'),
    path('my-order', my_order_view,name='my-order'),
    path('adminclick', adminclick_view),
    path('aboutus', aboutus_view),
    path('contactus', contactus_view, name='contactus'),
    path('my-profile',my_profile_view,name='my-profile'),
    path('edit-profile', edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', download_invoice_view,name='download-invoice'),


]
# + static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

