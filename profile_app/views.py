from django.shortcuts import render


def home(request):
    return render(request, 'profile_app/body.html')
