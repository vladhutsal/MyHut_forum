from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [

    path('', views.home_page, name='home_page'),
    path("topic/<slug:slug>/", views.topic_page, name="topic_page"),

    path("add_comment/<slug:slug>/", views.add_comment, name="add_comment"),
    path("my_hut/", views.myHut, name="user_room"),

    path("addTopic", views.addTopic, name="addTopic"),

    path("delete_comment/<int:comment_pk>/", views.delete_comment, name="delete_comment"),
    path('gain_delete_permission/<slug:slug>/', views.gain_delete_permission, name="gain_delete_perm"),

    path("comment_likes/<slug:slug>/<int:comment_id>/", views.comment_likes, name="likes"),

    path("api/", views.hello_world, name="api")
    
    
]

