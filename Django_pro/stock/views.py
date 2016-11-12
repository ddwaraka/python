from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# # Create your views here.
# def hello1(request):
#     return HttpResponse("Hello world")
#
# def hello2(request):
#     return HttpResponse("<h1>Hello World</h1>")
#



def hello3(request):
    return HttpResponse("Hello World at {}".format(datetime.now()))

# def hello4(request):
#     name = request.GET.get('name', "django")
#
#     return HttpResponse("Hello {}".format(name))


def hello1(request):

    return render(request, 'hello1.html')


def hello2(request):
    return render(request, 'hello2.html')


def hello4(request):
    context_dict = {'first_name': request.GET.get('first_name', 'django'), 'last_name': request.GET.get('last_name', 'python')}
    return render(request, 'hello4.html', context_dict)


def hello5(request):
    time_stamp = datetime.now()
    context_dict = {'time_stamp': datetime.now()}
    return render(request, 'hello3.html', context_dict)


def hello6(request):
    return render(request, 'submit.html')

