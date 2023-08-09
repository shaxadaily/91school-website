from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin




@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'created_at']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'text']


