from django.shortcuts import render


def weather_view(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


# Create your views here.
# https://openweathermap.org/history
# https://stackoverflow.com/questions/37721239/looking-for-a-weather-api-that-does-historical-forecast-data
# http://history.openweathermap.org/data/2.5/history/city?id={id}&type=hour&start={start}&cnt={cnt}