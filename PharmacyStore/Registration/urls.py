from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginForm,name="registration.login"),
    #There is set because it not accept duplicate
    path('signup/',views.signform,name="registration.signup"),
    path('store/',views.registrationStore,name="registration.store")
]
