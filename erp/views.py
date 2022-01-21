from django.shortcuts import render
from django.http import HttpResponse


def test_url_view(request):
    return HttpResponse('HOLA MUNDO!!!')
