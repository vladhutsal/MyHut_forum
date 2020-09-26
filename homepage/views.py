from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Count

from homepage.models import Topic, Comment, Tag
from homepage.forms import CommentForm, TopicForm

# add topic desription for 300 symbols

# Read views
def home_page(request):
    if request.user.is_authenticated is False:
        return redirect('login:user_login')
    else:
        form = TopicForm(None)
        annotated_topic_queryset = Topic.objects.annotate(comm_count=Count('comment'))
        context = {
            'name': request.user,
            'topic_queryset': annotated_topic_queryset,
            'form': form
            }
        return render(request, 'homepage/home_page.html', context)

def topic_page(request, topic_id):
    topic_object = Topic.objects.get(pk=topic_id)
    topic_comments = Comment.objects.filter(topic=topic_object)
    user = request.user
    has_delete_permition = user.has_perm('homepage.delete_comment')
    context = {
        'form': CommentForm,
        'topic_object': topic_object,
        'topic_comments': topic_comments,
        'has_delete_permition': has_delete_permition
    }
    return render(request, 'homepage/topics_page.html', context)


def myHut(request):
    return render(request, 'homepage/user_room.html')


# Create views
def add_comment(request, topic_id):
    if request.method == "POST":
        user = request.user
        text = request.POST.get('text')
        topic = Topic.objects.get(pk=topic_id)
        Comment.objects.create(user=user, text=text, topic=topic)
    return redirect('homepage:topic_page', topic_id=topic_id)

def addTopic(request):
    form = TopicForm(request.POST)
    if form.is_valid():
        topic = form.save(commit=False)
        topic.user = User.objects.get(username=request.user)
        topic.save()
        return redirect('homepage:topic_page', topic_id=topic.id)
    return redirect('homepage:home_page')


# Delete views
def delete_comment(request, comment_pk):
    current_comment = Comment.objects.get(pk=comment_pk)
    current_comment.delete()
    topic_id = current_comment.topic.id
    return redirect('homepage:topic_page', topic_id=topic_id)


# Update views
def delete_comment_permission(request, topic_id):
    content_type = ContentType.objects.get_for_model(Comment)
    permission = Permission.objects.get(
            codename="delete_comment",
            content_type=content_type,
        )
    user = request.user
    user.user_permissions.add(permission)
    return redirect('homepage:topic_page', topic_id=topic_id)


def comment_rating_change(request, topic_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    user = request.user
    if 'up' in request.POST:
        if user in comment.likes.all():
            pass
        else:
            comment.likes.add(user)
    elif 'down' in request.POST:
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            pass
    return redirect('homepage:topic_page', topic_id=topic_id)

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({
        'message': 'Hello world'
    })
