from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Registration


def test(request):
    return HttpResponse("Test Success - Learner's Permit")


def about(request):
    return HttpResponse("Test Success - About")


def contacts(request):
    return HttpResponse("Test Success - Contacts")


def clients(request):
    return HttpResponse("Test Success - Clients")


def index(request):
    """

    :param request:
    :return:
    """
    vr = Registration.objects.all()
    print(vr)
    return render(request, 'vr/index.html', {'vr': vr})
