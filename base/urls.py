from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginpage, name='login'),
    path('home', views.home, name='home'),
    path('temp', views.temp, name='temp'),
    path('humdt', views.humidity, name='humdt'),
    path('stress', views.stress, name='stress'),
    path('accl', views.accl, name='accl'),
    path('rainfall', views.rainfall, name='rainfall'),
    path('index', views.index, name='index'),
    path('err', views.err, name='404')
    ]




