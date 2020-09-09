from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from homepage.models import Topic, Comment, Tag
from homepage.forms import CommentForm

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
    current_topic = Topic.objects.get(pk=topic_id)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        user = request.user
        text = comment_form.data.get('text')
        Comment.objects.create(user=user, text=text, topic=current_topic)

    topic_comments = Comment.objects.filter(topic=current_topic)
    context = {
        'name': request.user,
        'form': comment_form,
        'topic_object': current_topic,
        'topic_comments': topic_comments
    }
    return render(request, 'homepage/topicpage.html', context)