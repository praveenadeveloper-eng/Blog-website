from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<slug:slug>/',views.edit_article,name='edit_article'),
    path('delete_article/<slug:slug>/',views.delete_article,name="delete_article")


]