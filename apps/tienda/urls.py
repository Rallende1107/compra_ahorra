from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'otaku_app'

urlpatterns = [
    # Otras URLs de tu proyecto...

    path('', views.HomeView, name='home'),

]