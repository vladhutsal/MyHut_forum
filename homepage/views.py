from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Topic, Comment
from .forms import CommentForm
from .serializers import TopicSerializer, CreateTopicSerializer


# auth decorator
def home_page(request):
    if request.user.is_authenticated is False:
        return redirect('login:user_login')
    else:
        return render(request, 'pages/home_page.html')


@api_view(['GET'])
def topic_list(request, *args, **kwargs):
    queryset = Topic.objects.all()
    serialized = TopicSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view(['POST'])
def create_topic(request):
    serialized = CreateTopicSerializer(data=request.POST)
    if serialized.is_valid(raise_exception=True):
        serialized.save(user=request.user)
        return Response(serialized.data, status=201)
    return Response({}, status=500)


def topic_page(request, slug):
    topic_object = get_object_or_404(Topic, slug=slug)

    topic_comments = Comment.objects.filter(topic=topic_object)
    user = request.user
    has_delete_permition = user.has_perm('homepage.delete_comment')
    context = {
        'form': CommentForm,
        'topic_object': topic_object,
        'topic_comments': topic_comments,
        'has_delete_permition': has_delete_permition
    }
    return render(request, 'pages/topics_page.html', context)


# Create views
def add_comment(request, slug):
    if request.method == "POST":
        user = request.user
        text = request.POST.get('text')
        topic = get_object_or_404(Topic, slug=slug)
        Comment.objects.create(user=user, text=text, topic=topic)
    return redirect('homepage:topic_page', slug=topic.slug)



# Delete views
def delete_comment(request, comment_pk):
    current_comment = Comment.objects.get(pk=comment_pk)
    current_comment.delete()
    slug = current_comment.topic.slug
    return redirect('homepage:topic_page', slug=slug)


# Update views
def gain_delete_permission(request, slug):
    content_type = ContentType.objects.get_for_model(Comment)
    permission = Permission.objects.get(
            codename="delete_comment",
            content_type=content_type,
        )
    user = request.user
    user.user_permissions.add(permission)
    return redirect('homepage:topic_page', slug=slug)
