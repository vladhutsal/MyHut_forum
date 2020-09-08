from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# create Topic
# organize by tags
# recent Topics
# search by title
# comments
# reccomend this topic? rating of topics

# count topics by user
# count all topics on main page


class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=5)
    title = models.CharField(max_length=100, unique=True)
    tags = models.ManyToManyField('Tag')
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{} ({})'.format(self.title, self.user)
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=5)
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
   

class RelatedComment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=5)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
