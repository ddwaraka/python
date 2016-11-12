# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def home_page(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        for task in tasks:
            print task.target_date
        return render(request, 'todo/home_page.html', {'tasks': Task.objects.all(), 'task_form': TaskForm()})

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_name = request.POST['task_name']
            task_priority = request.POST['task_priority']
            task_status = request.POST['task_status']
            target_date = request.POST['target_date']
            Task.objects.create(task_name=task_name, task_priority=task_priority, task_status=task_status,
                                target_date=target_date)
            return render(request, 'todo/home_page.html', {'user_message': 'Task {} successfully added'.format(task_name),
                                                           'tasks': Task.objects.all(), 'task_form': TaskForm()})
        else:
            return render(request, 'todo/home_page.html', {'tasks': Task.objects.all(), 'task_form': form})


# return HttpResponseRedirect('/')

# def add_task(request):
#     if request.method == 'GET':
#         return render(request, 'todo/add_task.html')
#
#     # if request.method == "POST":
#     #     movie_name = request.POST['movie_name']
#     #     Movie.objects.create(name=movie_name)
#     #     return HttpResponse('{} has been added to the database'.format(movie_name))
#
#     if request.method == "POST":
#         task_name = request.POST['task_name']
#         task_priority = request.POST['task_priority']
#         task_status = request.POST['task_status']
#         target_date = request.POST['target_date']
#         Task.objects.create(task_name=task_name, task_priority=task_priority, task_status=task_status,
#                             target_date=target_date)
#         return HttpResponse('Task has been added to the database')
#
#
# def view_task(request):
#     if request.method == 'GET':
#         context = dict()
#         context['task'] = Task.objects.all()
#         return render(request, 'todo/view_tasks.html', context)


def delete(request, task_id):
    if request.method == 'GET':
        # task_name = request.GET.get("delete", 'Nothing')
        # Task.objects.filter(id=id).delete()
        task = Task.objects.get(id=task_id)
        return render(request, 'todo/delete.html', {'task_name': task.task_name})

    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()
        return render(request,
                      'todo/home_page.html',
                      {'tasks': Task.objects.all(),
                       'task_form': TaskForm(),
                       'user_message': 'Task {} successfully deleted'.format(task.task_name)})


def edit(request, task_id):
    if request.method == 'GET':
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(initial={'task_name': task.task_name, 'task_priority': task.task_priority,
                             'task_status': task.task_status, 'target_date': task.target_date})

        return render(request, 'todo/edit_task.html', {'task': task, 'task_form': task_form})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.get(pk=task_id)
            task.task_name = form.cleaned_data['task_name']
            task.task_priority = form.cleaned_data['task_priority']
            task.task_status = form.cleaned_data['task_status']
            task.target_date = form.cleaned_data['target_date']
            task.save()
            return render(request, 'todo/home_page.html',
                          {'user_message': 'Task {} successfully edited'.format(task.task_name),
                           'tasks': Task.objects.all(), 'task_form': TaskForm()})
        else:

            return render(request, 'todo/edit_task.html', {'task_form': form})


def filter_name(request):
    if request.method == 'GET':
        task_name = request.GET['task_name']

        tasks = Task.objects.filter(task_name=task_name)
        return render(request, 'todo/filter_name.html', {'task_list': tasks, 'taskname': task_name})


def filter_priority(request):
    if request.method == 'GET':
        task_priority = request.GET['task_priority']

        tasks = Task.objects.filter(task_priority=task_priority)
        return render(request, 'todo/filter_priority.html', {'task_list': tasks, 'task_pri': task_priority})


def filter_status(request):
    if request.method == 'GET':
        task_status = request.GET['task_status']

        tasks = Task.objects.filter(task_status=task_status)
        return render(request, 'todo/filter_priority.html', {'task_list': tasks, 'task_status': task_status})






