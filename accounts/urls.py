from django.urls import path
from . import views

urlpatterns= [
    path('NewAccount', views.NewAccount, name='NewAccount'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('Book', views.Book, name='Book'),
]