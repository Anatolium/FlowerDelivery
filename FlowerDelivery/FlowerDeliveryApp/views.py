from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Это мой итоговый проект на Django</h2>")


def new(request):
    return HttpResponse("<h2>Это вторая страница моего итогового проекта на Django</h2>")

