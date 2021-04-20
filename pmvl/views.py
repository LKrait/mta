from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import PmvLicence


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
    pmvl = PmvLicence.objects.all()
    print(pmvl)
    return render(request, 'pmvl/index.html', {'pmvl': pmvl})
