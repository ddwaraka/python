from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is the app homepage</h1>")
