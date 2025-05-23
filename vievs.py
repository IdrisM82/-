import requests
from django.shortcuts import render
from forms import CityForm

def get_weather(request):
    weather_data = {}
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = 'a4a1fbf0c61e394ae13d3c5231be2026'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                }
            else:
                weather_data = {'error': 'City not found'}

        else:
            form = CityForm()

        return render(request, 'weathvpython manage.py runserverpython manage.py runserverpython manage.py runserverer/weather.html', {'form': form, 'weather_data': weather_data})