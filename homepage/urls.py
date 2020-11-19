from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [

    path('', views.home_page, name='home_page'),

    path('api/topics/', views.topic_list),
    path('api/topics/create', views.create_topic),
    path('api/comments/<int:comment_id>/like', views.handle_comment_likes),

    # old path
    path("topic/<int:topic_id>/", views.topic_page, name="topic_page"),
    path("add_comment/<int:topic_id>/", views.add_comment, name="add_comment"),
    path("delete_comment/<int:comment_pk>/", views.delete_comment, name="delete_comment"),
    # path('gain_delete_permission/<int:topic_id>/', views.gain_delete_permission, name="gain_delete_perm")
    
    
]

