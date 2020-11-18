from django.shortcuts import render
import requests


def my_hut(request):
    token = 'dbccac2b303dc8ed21da417f693f9f63'
    city = 'Dnipro'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={token}'
    response = requests.get(url).json()
    response['weather'] = response['weather'][0]

    # weather id, main, description
    # name
    # main temp feels_like

    weather_dict = {
        'weather_icon': response['weather']['icon'],
        'weather_descr': response['weather']['description'],
        'city': response['name'],
        'temp': response['main']['temp'],
    }
    return render(request, 'pages/user_room.html')
