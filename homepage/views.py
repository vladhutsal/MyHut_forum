from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from homepage.models import Topic, Comment, Tag
from homepage.forms import CommentForm, TopicForm

# return render(request, 'homepage/error.html', {'error': })

# Page views
def home_page(request):
    if request.user.is_authenticated is False:
        return redirect('login:user_login')
    else:
        topic_names = Topic.objects.all()

        context = {
            'name': request.user,
            'topic_names': topic_names
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


def test(request):
    return render(request, 'homepage/test.html')


# Topic views
def add_topic(request):
    form = TopicForm(request.POST or None)
    if form.is_valid():
        topic = form.save(commit=False)
        topic.user = User.objects.get(username=request.user)
        topic.save()
        print(topic)
        return redirect('homepage:home_page')
    context = {
        'form': form
    }
    return render(request, 'homepage/add_topic.html', context)


# Comment views
def add_comment(request, topic_id):
    if request.method == "POST":
        user = request.user
        text = request.POST.get('text')
        topic = Topic.objects.get(pk=topic_id)
        Comment.objects.create(user=user, text=text, topic=topic)
    return redirect('homepage:topic', topic_id=topic_id)


def delete_comment(request, comment_id):
    current_comment = Comment.objects.get(id=comment_id)
    current_comment.delete()
    topic_id = current_comment.topic.id
    return redirect('homepage:topic', topic_id=topic_id)


def delete_comment_permission(request, topic_id):
    content_type = ContentType.objects.get_for_model(Comment)
    permission = Permission.objects.get(
            codename="delete_comment",
            content_type=content_type,
        )
    user = request.user
    user.user_permissions.add(permission)
    return redirect('homepage:topic', topic_id=topic_id)
