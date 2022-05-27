from django.urls import path

from . import views

urlpatterns = [ 
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('',views.Find_mean_mode_median, name="Find_mean_mode_median"),
    ]