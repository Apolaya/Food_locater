from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_with_template, name='home_with_template'),
    path('button/', views.button_action, name='button_page'), 
    path('square/', views.square_clicked, name = 'square_post' ),
]