from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Lesson, Courses
from .forms import LessonForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, FileResponse
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

# Create your views here.
# def index(request):
#     return render(request, 'main/index.html')


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main/index.html")


def create(request, courseid):
    error = ''
    if request.method == 'POST':
        lesson = Lesson()
        lesson.course_id = request.POST.get('course')
        lesson.number = request.POST.get('number')
        lesson.title = request.POST.get('title')
        lesson.description = request.POST.get('description')
        lesson.presentation_file = request.FILES.get('presentation_file')
        lesson.save()
        return redirect("/courseslist/{}".format(request.POST.get('course')))
    courses = Courses.objects.all()
    context = {
        'courseid': courseid,
        'courses': courses,
        'error': error
    }
    return render(request, 'main/create.html', context)


class CreateLessonView(CreateView):
    form_class = LessonForm
    template_name = "main/create.html"
    success_url = reverse_lazy("alllessonsofcourse")


class UpdateLessonView(UpdateView):
    model = Lesson
    fields = ["course","number", "title", "description","presentation_file"]


class DeleteLessonView(DeleteView):
    model = Lesson
    success_url = "main/allcourses.html"

# Добавить класс Update и Delete 


def edit(request, courseid, lessonid):
    error = ''
    try:
        lesson = Lesson.objects.get(id = lessonid)
        if request.method == "POST":
            lesson.course_id = request.POST.get('course')
            lesson.number = request.POST.get('number')
            lesson.title = request.POST.get('title')
            lesson.description = request.POST.get('description')
            lesson.presentation_file = request.FILES.get('presentation_file')
            lesson.save()
            return redirect("/courseslist/{}".format(request.POST.get('course')))
        courses = Courses.objects.all()
        context = {
            'courseid': courseid,
            'courses': courses,
            'lesson': lesson,
            'error': error
        }
        return render(request, 'main/edit.html', context)

    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")



def delete(request, courseid, lessonid):
    try:
        lesson = Lesson.objects.get(id = lessonid)
        lesson.delete()
        return redirect("/courseslist/{}".format(courseid))
    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


class Lessons(ListView):
    model = Lesson
    context_object_name = "lessons"
    template_name = "main/lessons.html"
    def get_queryset(self):
        return Lesson.objects.filter(course__slug=self.kwargs.get("slug")).select_related('course')


class AllLessonsOfCourse(ListView):
    model = Lesson
    context_object_name = "lessons"
    template_name = "main/alllessonsofcourse.html"

    def get_queryset(self):
        return Lesson.objects.filter(course__slug=self.kwargs.get("slug")).select_related('course')


class Course(ListView):
    model = Courses
    context_object_name = "courses"
    template_name = "main/courses.html"


class AllCourses(ListView):
    model = Courses
    context_object_name = "courses"
    template_name = "main/allcourses.html"