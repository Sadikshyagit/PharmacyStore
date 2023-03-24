from django.urls import path
from . import views


urlpatterns = [
    path('doclogin/',views.loginForm,name="doctor.login"),
    #There is set because it not accept duplicate
    path('docsignup/',views.SignupPage,name="docto.signup"),
]
