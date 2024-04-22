from django.shortcuts import render, redirect
from .models import Lesson, Courses
from .forms import LessonForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, FileResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def showlessons(request):
    return render(request, 'main/showlessons.html')


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


def lessons(request, courseid, lessonid):
    if lessonid == 0:
        lessons = Lesson.objects.filter(course = courseid)
        context = {
            'lessons': lessons
        }
        return render(request, 'main/lessons.html', context)
    
    lessons = Lesson.objects.filter(course = courseid)
    lesson = Lesson.objects.get(id = lessonid)
    context = {
        'lessonid': lessonid,
        'lesson': lesson,
        'lessons': lessons
    }
    return render(request, 'main/lessons.html', context)


def lessonslist(request, courseid):
    lessons = Lesson.objects.filter(course = courseid)
    course = Courses.objects.get(id = courseid)
    context = {
        'lessons': lessons,
        'course': course
    }
    return render(request, 'main/lessonslist.html', context)


def courses(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'main/courses.html', context)


def courseslist(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'main/courseslist.html', context)