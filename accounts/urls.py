from django.urls import path, include
from .views import *


urlpatterns = [
    path('', myAccount),
    path('register-user/', registerUser, name='register_user'),
    path('register-vendor/', registerVendor, name='register_vendor'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('my-account/', myAccount, name='my_account'),
    path('customer-dashboard/', customerDashboard, name='customer_dashboard'),
    path('vendor-dashboard/', vendorDashboard, name='vendor_dashboard'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path('forgot-password/', forgotPassword, name='forgot_password'),
    path('reset-password_validate/<uidb64>/<token>/', resetPasswordValidate, name='reset_password_validate'),
    path('reset-password/', resetPassword, name='reset_password'),

    path('vendor/', include('vendors.urls')),
]