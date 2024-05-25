from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from .models import Lesson, Courses, AvailableLessons, CommentsOnLesson
from .forms import LessonForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, FileResponse, Http404
import random
import string

# Главная страница.
@login_required
def index(request):
    return render(request, 'main/index.html')

# Редактирование
@login_required
def create(request, course_slug):
    error = ''
    course_id = Courses.objects.get(slug = course_slug).id
    lesson_form = LessonForm(initial={'course': course_id})
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, request.FILES)
        if lesson_form.is_valid():
            lesson_form.save()
            return redirect("/courses_list/{}".format(course_slug))
        else:
            error = "Форма была некорректна"
    context = {
        'form': lesson_form,
        'error': error,
        'type': 'create',
    }
    return render(request, 'main/create.html', context)


@login_required
def edit(request, course_slug, lesson_id):
    error = ''
    try:
        lesson = Lesson.objects.get(id = lesson_id)
        lesson_form = LessonForm(instance = lesson)
        if request.method == "POST":
            lesson_form = LessonForm(request.POST, request.FILES, instance=lesson)
            if lesson_form.is_valid():
                lesson_form.save()
                return redirect("/courses_list/{}".format(course_slug))
            else:
                error = "Форма была некорректна"
        context = {
            'form': lesson_form,
            'error': error,
            'type': 'edit',
        }
        return render(request, 'main/create.html', context)

    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


@login_required
def deleteLesson(request, course_slug, lesson_id):
    try:
        lesson = Lesson.objects.get(id = lesson_id)
        lesson.delete()
        return redirect("/courses_list/{}".format(course_slug))
    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
    

@login_required
def deleteLink(request, course_slug, link_id):
    try:
        lesson = AvailableLessons.objects.get(id = link_id)
        lesson.delete()
        return redirect("/courses_list/{}".format(course_slug))
    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

@login_required
def create_link(request, course_slug, lesson_id):
    sluggen = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(12)])
    passwordgen = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(12)])
    AvailableLessons.objects.create(
        lesson = Lesson.objects.get(id = lesson_id),
        slug = sluggen,
        link = "http://127.0.0.1:8000/availablelesson/" + sluggen,
        password = passwordgen,
        is_active = False,
    )
    context = {
        'slug': sluggen,
        'password': passwordgen,
    }
    return render(request, 'main/readylink.html', context)


@login_required
def courses_list(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'main/courses_list.html', context)

@login_required
def lessons_list(request, course_slug):
    lessons = Lesson.objects.filter(course__slug = course_slug)
    course = Courses.objects.get(slug = course_slug)
    available_lessons = AvailableLessons.objects.filter(lesson__course__slug = course_slug)
    context = {
        'lessons': lessons,
        'course': course,
        'available_lessons': available_lessons,
    }
    return render(request, 'main/lessons_list.html', context)

# Просмотр
@login_required
def lessons(request, course_slug, lesson_id):
    if lesson_id == 0:
        lessons = Lesson.objects.filter(course__slug = course_slug).order_by('number').values()
        context = {
            'lessons': lessons
        }
        return render(request, 'main/lessons.html', context)
    
    lessons = Lesson.objects.filter(course__slug = course_slug).order_by('number').values()
    lesson = Lesson.objects.get(id = lesson_id)
    context = {
        'lesson_id': lesson_id,
        'lesson': lesson,
        'lessons': lessons
    }
    return render(request, 'main/lessons.html', context)

def get_lesson(lesson_slug):
    lesson = AvailableLessons.objects.get(slug = lesson_slug)
    comments = CommentsOnLesson.objects.filter(lesson__slug = lesson_slug).order_by("-date")
    context = {
        'lesson': lesson,
        'comments': comments,
    }
    return context

def available_lesson(request, lesson_slug):
    password_for_lesson = AvailableLessons.objects.get(slug = lesson_slug).password
    context = {
        'error': ''
    }
    if request.method == 'POST':
        if 'check_password' in request.POST:
            if password_for_lesson == request.POST.get('password'):
                request.session[lesson_slug] = True
                context = get_lesson(lesson_slug)
                return render(request, 'main/availablelesson.html', context)
            else:
                context = {
                    'error': "Неверный пароль"
                }
                return render(request, 'main/accesstolesson.html', context)
        elif 'create_comment' in request.POST:
            if request.user.is_superuser:
                request.session[lesson_slug] = True
            elif request.session.get(lesson_slug) != True:
                return render(request, 'main/accesstolesson.html', context)
            comment = CommentsOnLesson()
            comment.lesson = AvailableLessons.objects.get(slug = lesson_slug)
            comment.author = request.POST.get('comment_author')
            comment.comment = request.POST.get('comment_text')
            comment.save()
            context = get_lesson(lesson_slug)
            return render(request, 'main/availablelesson.html', context)
        
    if request.user.is_superuser:
        context = get_lesson(lesson_slug)
        return render(request, 'main/availablelesson.html', context)

    if request.session.get(lesson_slug) == True:
        context = get_lesson(lesson_slug)
        return render(request, 'main/availablelesson.html', context)
    
    return render(request, 'main/accesstolesson.html', context)

@login_required
def courses(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'main/courses.html', context)


def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

#rWl1aMPd
# @login_required
def secure_file_read(request, filename):
    obj = Lesson.objects.filter(presentation_file = f'pptxfiles/{filename}').first()
    if obj:
        return FileResponse(obj.presentation_file)
