from django.contrib import admin
from .models import Post

# make Post visible on admin page
admin.site.register(Post)