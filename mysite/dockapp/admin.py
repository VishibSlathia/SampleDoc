from django.contrib import admin
from .models import TodoItem, ToListenSongs
# Register your models here.

admin.site.register(TodoItem)
admin.site.register(ToListenSongs)