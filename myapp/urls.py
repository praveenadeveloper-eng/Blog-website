from . import views
from django.urls import path

app_name='myapp'

urlpatterns=[
    path('',views.home,name='home'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('post_list/',views.post_list,name="post_list"),
    
]