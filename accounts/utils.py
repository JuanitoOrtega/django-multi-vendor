def detecUser(user):
    if user.role == 1:
        redirectUrl = 'vendor_dashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'customer_dashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl