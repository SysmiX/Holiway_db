from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Holiway! You're at the polls index.")