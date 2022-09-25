import json
from django.shortcuts import render
from weather.forms import GetWeatherForm
from testify.settings import WEATHER_KEY
from django.http import HttpResponse
import requests


def weather_view(request):
    if request.method == 'GET':

        # If no data was given in GET params, render default form
        if not request.GET:
            form = GetWeatherForm()
            return render(request, 'weather_form.html', context={'form': form})

        # Else, validate form
        else:
            form = GetWeatherForm(request.GET)

            # if form is valid, get data from OpenWeatherMap API
            if form.is_valid():
                city = form.cleaned_data['city']
                str_date = form.cleaned_data['date']

                # Current API KEY is trial, so request won't work correctly
                response = requests.get(
                    f'https://api.openweathermap.org/data/2.5/history/city?q={city}&type=hour&start={str_date}&cnt=1&appid={WEATHER_KEY}'
                )

                # Without subscription, this response won't give any weather data (response is JSON)
                return HttpResponse(json.dumps(response.json()), content_type='application/json')

            # If form is invalid, let user know what went wrong
            return render(request, 'weather_form.html', context={'form': form})
