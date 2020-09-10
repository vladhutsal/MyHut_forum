from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path("test", views.test, name="test"),
    path("topic/<int:topic_id>", views.topic_page, name="topic"),
    path("add_topic", views.add_topic, name="add_topic")
    
]

urlpatterns += staticfiles_urlpatterns()
