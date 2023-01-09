from django.urls import path, include
from .views import *


urlpatterns = [
    path('', myAccount),
    path('register_user/', registerUser, name='register_user'),
    path('register_vendor/', registerVendor, name='register_vendor'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('my_account/', myAccount, name='my_account'),
    path('customer_dashboard/', customerDashboard, name='customer_dashboard'),
    path('vendor_dashboard/', vendorDashboard, name='vendor_dashboard'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path('forgot_password/', forgotPassword, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', resetPasswordValidate, name='reset_password_validate'),
    path('reset_password/', resetPassword, name='reset_password'),

    path('vendor/', include('vendors.urls')),
]