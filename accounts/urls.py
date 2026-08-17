from django.urls import path

from . import views

app_name='accounts'

urlpatterns=[
    path('register/',views.register,name="register"),
    path('login_page/',views.login_page,name="login_page"),
    path('logout_page/',views.logout_page,name='logout_page')
]