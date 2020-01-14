from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Это поле обязательно')

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', )
    
class RenewFlowerForm(forms.Form):
    renewal_date = forms.DateField(help_text="Введите дату доставки")
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
        if data < datetime.date.today():
            raise ValidationError(_('Неверная дата'))

        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=12):
            raise ValidationError(_('Неверная дата - мы не можем обеспечить заказ более чем через месяц'))

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data

class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
