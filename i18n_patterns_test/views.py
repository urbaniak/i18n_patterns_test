from django.http import HttpResponse


def index(request):
    return HttpResponse("lang: {}".format(request.LANGUAGE_CODE))


def test(request, city):
    return HttpResponse("lang: {} city: {}".format(request.LANGUAGE_CODE, city))
