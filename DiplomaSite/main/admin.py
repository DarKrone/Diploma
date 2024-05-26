from typing import Any
from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Lesson, Courses, AvailableLessons, CommentsOnLesson, Answer, Question

# class LessonsInline(admin.StackedInline):
#     model = Lesson
#     extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "course", "number", "title"]
    ordering = ['course', 'number']

@admin.register(AvailableLessons)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["id", "lesson"]
    orderind = ['id']

admin.site.register(Courses)
admin.site.register(Answer)
admin.site.register(Question)

@admin.register(CommentsOnLesson)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "get_lesson", "author", "date", "short_comment"]
    orderind = ['id']

    @admin.display(ordering='lesson__title', description='Lesson')
    def get_lesson(self, obj):
        return obj.lesson.lesson.title
    
