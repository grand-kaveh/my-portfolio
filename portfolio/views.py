from django.shortcuts import render
from django.conf import settings


# url: /
def home_page(request):
    return render(request, 'portfolio/home.html', {})


def save_contact_form(request):
    print(settings.APIKEY_IPIFY)