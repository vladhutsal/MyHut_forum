from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from homepage.models import Topic, Comment, Tag
from homepage.forms import CommentForm, TopicForm

# return render(request, 'homepage/error.html', {'error': })

def home(request):
    if request.user.is_authenticated is False:
        return redirect('login:user_login')
    else:
        topic_names = Topic.objects.all()
        context = {
            'name': request.user,
            'topic_names': topic_names
            }
        return render(request, 'homepage/home.html', context)

def test(request): 
    return render(request, 'homepage/test.html')

def topic_page(request, topic_id):
    topic_object = Topic.objects.get(pk=topic_id)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        user = request.user
        text = comment_form.data.get('text')
        Comment.objects.create(user=user, text=text, topic=topic_object)

    topic_comments = Comment.objects.filter(topic=topic_object)
    context = {
        'form': comment_form,
        'topic_object': topic_object,
        'topic_comments': topic_comments
    }
    return render(request, 'homepage/topics_page.html', context)

def delete_comment(request, comment_id):
    current_comment = Comment.objects.get(id=comment_id)
    current_comment.delete()
    topic_id = current_comment.topic.id
    return redirect('homepage:topic', topic_id=topic_id)


def add_topic(request):
    form = TopicForm(request.POST or None)
    if form.is_valid():
        topic = form.save(commit=False)
        topic.user = User.objects.get(username=request.user)
        topic.save()
        print(topic)
        return redirect('homepage:home')
    context = {
        'form': form
    }
    return render(request, 'homepage/add_topic.html', context)
