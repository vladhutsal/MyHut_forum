from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify


# organize by tags
# recent Topics
# search by title
# reccomend this topic? rating of topics


class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()

    comments_count = models.PositiveIntegerField(blank=True, default=0)
    tags = models.ManyToManyField('Tag', blank=True)

    image = models.ImageField(null=True, blank=True)
    # rating = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return '{} - {} - ({})'.format(self.pk, self.title, self.user)

    def truncate_text(self):
        pass


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True,
                                   related_name="comment_likes")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return 'User: {}, Topic: {}'.format(self.user, self.topic)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    queryset = Topic.objects.filter(slug=slug).order_by('-id')
    topic_obj = queryset.first()
    exists = queryset.exists()
    if exists:
        new_slug = f'{slug}-{topic_obj.id}-{topic_obj.user}'
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_topic(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_topic, sender=Topic)
