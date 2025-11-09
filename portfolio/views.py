from django.shortcuts import render


# url: /
def home_page(request):
    return render(request, 'portfolio/home.html', {})