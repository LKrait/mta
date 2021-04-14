from django.shortcuts import render
from django.http import HttpResponse
from .models import Licence


def index(request):
    """

    :param request:
    :return:
    """
    pl = Licence.objects.all()
    print(pl)
    return render(request, 'pl/index.html', {'pl': pl})
