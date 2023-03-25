from django.urls import path
from . import views


urlpatterns = [
    path('pharlogin/',views.loginForm,name="phar.login"),
    #There is set because it not accept duplicate
    path('pharsignup/',views.SignupPage,name="phar.signup"),
]
