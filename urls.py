from vievs import get_weather
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', get_weather, name='get_weather'),
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
]




