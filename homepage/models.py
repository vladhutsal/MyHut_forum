from django import forms
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse

# organize by tags
# recent Topics
# search by title
# reccomend this topic? rating of topics

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    tags = models.ManyToManyField('Tag', blank=True)
    text = models.TextField()


    def __str__(self):
        return '{} ({})'.format(self.title, self.user)
    
    def get_absolute_url(self):
        return reverse("homepage:topic_page", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name="comment_likes")
    

    def __str__(self):
        return 'comment: {}, user: {}, topic: {}'.format(self.text, self.user, self.topic)
    
   
class RelatedComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
