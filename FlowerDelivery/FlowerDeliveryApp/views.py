from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>Это мой итоговый проект на Django</h1>")
    return render(request, 'FlowerDeliveryApp/index.html')


def new(request):
    # return HttpResponse("<h2>Это вторая страница моего итогового проекта на Django</h2>")
    return render(request, 'FlowerDeliveryApp/new.html')
