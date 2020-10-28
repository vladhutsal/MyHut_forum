from django.contrib import admin

from homepage.models import Topic, Comment

admin.site.register(Topic)
admin.site.register(Comment)


class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', "updated", ]
