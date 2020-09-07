from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path("test", views.test, name="test"),
]

urlpatterns += staticfiles_urlpatterns()
