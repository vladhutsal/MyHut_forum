from django.urls import path
from . import views

app_name = 'my_hut'

urlpatterns = [
    path("", views.my_hut, name='my_hut')
]
