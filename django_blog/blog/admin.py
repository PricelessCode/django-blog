from django.contrib import admin
from .models import Post

# Register your models here.

# If you put the model here you will be able to see it on /admin site
admin.site.register(Post)