from os import name
from django.urls import path
from Users.views import UserLogin, RegisterView,templateInicio

#IMPORTAR LOGOUT
from django.contrib.auth.views import LogoutView  



urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', UserLogin.as_view(),name='login'),
    path("logout/",LogoutView.as_view(next_page="login"),name="logout"),
    path('', templateInicio.as_view(),name='Inicio'),
   

]