from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'caption': "FlowerDelivery"
    }
    return render(request, 'FlowerDeliveryApp/index.html', data)


def new(request):
    # return HttpResponse("<h2>Это вторая страница моего итогового проекта на Django</h2>")
    return render(request, 'FlowerDeliveryApp/new.html')
