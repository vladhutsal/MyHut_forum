from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path("test", views.test, name="test"),
    path('', views.home_page, name='home'),
    path("topic/<int:topic_id>", views.topic_page, name="topic"),

    path("add_comment/<int:topic_id>", views.add_comment, name="add_comment"),
    path("delete_comment/<int:comment_id>", views.delete_comment, name="delete_comment"),
    path('delete_comment_perm/<int:topic_id>', views.delete_comment_permission, name="gain_delete_perm"),
    path("comment_rating_change/<int:topic_id>/<int:comment_id>/", views.comment_rating_change, name="comment_rating_change")
    
    
]

urlpatterns += staticfiles_urlpatterns()
