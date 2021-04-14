from django.shortcuts import render


def style(request):
    """
    :param request:
    :return:
    """
    return render(request, 'base/all.css')
