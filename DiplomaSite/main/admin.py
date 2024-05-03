from typing import Any
from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Lesson, Courses, AvailableLessons

# class LessonsInline(admin.StackedInline):
#     model = Lesson
#     extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["course", "number", "title"]
    ordering = ['course', 'number']

admin.site.register(Courses)
admin.site.register(AvailableLessons)
