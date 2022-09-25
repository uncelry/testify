from django import forms


class GetWeatherForm(forms.Form):
    """Weather search input form"""
    city = forms.CharField(max_length=50, label='Город (латиница)', widget=forms.TextInput(attrs={'placeholder': 'Moscow'}))
    date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}, format=('%Y-%m-%d')))
