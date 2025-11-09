from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .models import (
    InfoModel,
    SkillModel,
    DegreeModel,
    PortfolioModel,
    PackageModel,
    ContactModel,
)
from extentions.utils import get_client_ip


# url: /
def home_page(request):
    contact_form = ContactForm(request.POST or None)

    if request.POST:
        if contact_form.is_valid():
            ContactModel.objects.create(
                ip=get_client_ip(request=request),
                name=contact_form.cleaned_data.get('name'),
                email_address=contact_form.cleaned_data.get('email_address'),
                message=contact_form.cleaned_data.get('message'), 
            )
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


# url: /get-ip-data
@login_required(login_url='/403')
def get_ip_data(request):
    print(settings.APIKEY_IPIFY)