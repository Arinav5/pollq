from django.contrib import admin

from .models import Post, Choice

admin.site.register([Post, Choice])