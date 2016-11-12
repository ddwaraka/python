
from django.shortcuts import render
from .models import StockName
from django.contrib.auth.decorators import login_required
from .forms import AddForm

# Create your views here.


def profile(request):

    return render(request, 'profile.html')


def homepage(request):
    return render(request, 'homepage.html')


@login_required
def dashboard(request):
    if request.method == 'GET':
        stock_names = StockName.objects.filter(user=request.user)
        username = request.user.first_name
        return render(request, 'dashboard.html', {'stock_names': stock_names, 'add_form': AddForm(),
                                                  'user_name': username})

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            company_code = request.POST['company_code']
            target_price = request.POST['target_price']
            StockName.objects.create(company_code=company_code, target_price=target_price, user=request.user)
            username = request.user.first_name
            return render(request, 'dashboard.html', {'stock_names': StockName.objects.filter(user=request.user),
                                                      'add_form': AddForm(),
                                                      'user_name': username})


def delete(request, stock_id):
    if request.method == 'GET':
        print "executing"
        stock = StockName.objects.get(id=stock_id)
        return render(request, 'delete.html')









