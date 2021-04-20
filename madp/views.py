from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import MorobeAdministrationDrivingPermit


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
    madp = MorobeAdministrationDrivingPermit.objects.all()
    print(madp)
    return render(request, 'madp/index.html', {'madp': madp})
