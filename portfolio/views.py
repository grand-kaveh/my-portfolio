from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import (
    InfoModel,
    SkillModel,
    DegreeModel,
    PortfolioModel,
    PackageModel,
)
from extentions.utils import get_client_ip


# url: /
def home_page(request):
    contact_form = ContactForm(request.POST or None, initial={'ip': get_client_ip(request)})

    if request.POST:
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank You for Submission!')
            return redirect('/')


    context = {
        'skills1': SkillModel.objects.all()[0:SkillModel.objects.count()/2],
        'skills2': SkillModel.objects.all()[SkillModel.objects.count()/2:],
        'degrees': DegreeModel.objects.all(),
        'ports': PortfolioModel.objects.all(),
        'info': InfoModel.objects.last(),
        'apps': PackageModel.objects.all(),
        'form': contact_form,
    }

    return render(request, 'portfolio/home.html', context)


def save_contact_form(request):
    print(settings.APIKEY_IPIFY)