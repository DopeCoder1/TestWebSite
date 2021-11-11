from django.urls import path
from .views import createRegister
urlpatterns = [
    path('', createRegister,name='home'),
]