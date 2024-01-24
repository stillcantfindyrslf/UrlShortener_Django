from django.urls import path
from .views import home, createShortURL, about, FAQ, redirect


urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortURL, name='create'),
    path('about', about, name='about'),
    path('FAQ', FAQ, name='faq.html'),
    path('<str:url>', redirect, name='redirect')
]