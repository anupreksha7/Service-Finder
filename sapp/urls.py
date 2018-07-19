from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/',views.results, name='results'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/userlogin/', views.userlogin, name='userlogin'),
    path('login/providerlogin/', views.prologin, name='prologin'),
    path('logout/', views.logout, name='logout'),
    path('results/book/', views.book, name='book'),
    path('userhome/', views.user_page, name = 'user_page'),
    path('providerhome/', views.provider_page, name = 'provider_page'),
    path('contribute/', views.contribute, name = 'contribute')
]
