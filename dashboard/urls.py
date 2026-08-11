from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]