from django.contrib.auth.views import LoginView
from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('<str:shorted_url>', views.redirect_from_shorted_url, name='redirect_from_shorted_url'),
    path('add_url/', views.add_shorted_url, name='add_url'),
    path('remove_url/<int:id>', views.remove_shorted_link, name='remove_url'),
]