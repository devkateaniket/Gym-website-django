from django.urls import path

from .views import home, join_gym, login_view, logout_view, signup_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('join/', join_gym, name='join_gym'),
]
