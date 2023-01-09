from django.shortcuts import render


def vProfile(request):
    return render(request, 'vendors/v_profile.html')