# coding: utf-8
from django.contrib import admin
from mysite.todo.models import Category, Todo

#admin.site.register(Category)
#admin.site.register(Todo)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
admin.site.register(Category, CategoryAdmin)


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'datetime_created', 'is_finished', 'priority', 'category', )
    list_display_links = ('id', 'title',)
admin.site.register(Todo, TodoAdmin)
