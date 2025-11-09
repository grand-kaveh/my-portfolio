from django.shortcuts import render


def page_404(request):
    return render(request, '404.html', {})


def page_403(request):
    return render(request, '403.html', {})


def page_503(request):
    return render(request, '503.html', {})

