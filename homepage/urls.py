from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [

    path('', views.home_page, name='home_page'),
    path("topic/<slug:slug>/", views.topic_page, name="topic_page"),

    path("add_comment/<slug:slug>/", views.add_comment, name="add_comment"),
    path("add_topic", views.add_topic, name="add_topic"),

    path("delete_comment/<int:comment_pk>/", views.delete_comment, name="delete_comment"),
    path('gain_delete_permission/<slug:slug>/', views.gain_delete_permission, name="gain_delete_perm")
    
    
]

