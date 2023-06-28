from django.contrib import admin, sites
from .models import Post, Like, User
# Register your models here.
# admin.site.register(User)
admin.site.register(Post)
admin.site.register(Like)
