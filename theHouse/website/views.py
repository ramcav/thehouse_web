from django.shortcuts import render
from django.conf import settings
from django.views import View
from .models import User

class LandingView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'website/mockup.html', context)

class Waitlist(View):
    def post(self, request):
        model = User
        
        return render(request, 'website/mockup.html') 
        