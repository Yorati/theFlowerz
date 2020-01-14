from django.shortcuts import render
from .models import  Flower, KindOfFlower, Color, ForSale
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewFlowerForm

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
    username = form.cleaned_data.get('username')
    my_password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=my_password)
    login(request, user)
    return redirect('index')
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_flowers=Flower.objects.all().count()
    num_for_sale=ForSale.objects.all().count()
    # Доступные книги (статус = 'o')
    num_for_sale_available=ForSale.objects.filter(status__exact='o').count()
    num_kindofflower=KindOfFlower.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_flowers':num_flowers,'num_for_sale':num_for_sale,'num_for_sale_available':num_for_sale_available,'num_kindofflower':num_kindofflower},
    )

class FlowerListView(generic.ListView):
    model = Flower
    paginate_by = 5
class FlowerDetailView(generic.DetailView):
    model = Flower
class LoanedFlowersByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = ForSale
    template_name ='catalog/forsale_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return ForSale.objects.filter(borrower=self.request.user).filter(status__exact='o')
