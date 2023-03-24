from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginForm,name="registration.login"),
    path('',views.firstpage, name="first"),
    #There is set because it not accept duplicate
    path('signup/',views.SignupPage,name="registration.signup"),
    # path('store/',views.registrationStore,name="registration.store")
]
