from django.urls import path

from .views import home, join_gym


urlpatterns = [
    path('', home, name='home'),
    path('join/', join_gym, name='join_gym'),
]
