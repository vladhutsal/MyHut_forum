from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("topic/<slug:slug>/", views.topic_page, name="topic_page"),

    path("add_comment/<slug:slug>/", views.add_comment, name="add_comment"),
    path("addTopic", views.addTopic, name="addTopic"),

    path("delete_comment/<int:comment_pk>/", views.delete_comment, name="delete_comment"),
    path('delete_comment_perm/<int:topic_id>/', views.delete_comment_permission, name="gain_delete_perm"),

    path("comment_rating_change/<int:topic_id>/<int:comment_id>/", views.comment_rating_change, name="comment_rating_change"),

    path("api/", views.hello_world, name="api")
    
    
]

