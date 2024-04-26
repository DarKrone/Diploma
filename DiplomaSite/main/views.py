from django.shortcuts import render, redirect
from .models import Lesson, Courses
from .forms import LessonForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, FileResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def show_lessons(request):
    return render(request, 'main/show_lessons.html')


def create(request, course_id):
    error = ''
    lesson_form = LessonForm(initial={'course': course_id})
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, request.FILES)
        if lesson_form.is_valid():
            lesson_form.save()
            return redirect("/courses_list/{}".format(request.POST.get('course')))
        else:
            error = "Форма была некорректна"
    context = {
        'form': lesson_form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def edit(request, course_id, lesson_id):
    error = ''
    try:
        lesson = Lesson.objects.get(id = lesson_id)
        lesson_form = LessonForm(instance = lesson)
        if request.method == "POST":
            lesson_form = LessonForm(request.POST, request.FILES, instance=lesson)
            if lesson_form.is_valid():
                lesson_form.save()
                return redirect("/courses_list/{}".format(request.POST.get('course')))
            else:
                error = "Форма была некорректна"
        context = {
            'form': lesson_form,
            'error': error,
        }
        return render(request, 'main/edit.html', context)

    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def delete(request, course_id, lesson_id):
    try:
        lesson = Lesson.objects.get(id = lesson_id)
        lesson.delete()
        return redirect("/courses_list/{}".format(course_id))
    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def lessons(request, course_id, lesson_id):
    if lesson_id == 0:
        lessons = Lesson.objects.filter(course = course_id)
        context = {
            'lessons': lessons
        }
        return render(request, 'main/lessons.html', context)
    
    lessons = Lesson.objects.filter(course = course_id)
    lesson = Lesson.objects.get(id = lesson_id)
    context = {
        'lesson_id': lesson_id,
        'lesson': lesson,
        'lessons': lessons
    }
    return render(request, 'main/lessons.html', context)


def lessons_list(request, course_id):
    lessons = Lesson.objects.filter(course = course_id)
    course = Courses.objects.get(id = course_id)
    context = {
        'lessons': lessons,
        'course': course
    }
    return render(request, 'main/lessons_list.html', context)


def courses(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'main/courses.html', context)


def courses_list(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'main/courses_list.html', context)