from django import forms


class GetWeatherForm(forms.Form):
    city = forms.CharField(max_length=50, help_text='Город')
    date = forms.DateField(help_text='Дата')