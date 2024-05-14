from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('courses_list/<slug:course_slug>/edit/<int:lesson_id>/', views.edit, name = 'edit'),
    path('courses_list/<slug:course_slug>/deletelesson/<int:lesson_id>/', views.deleteLesson, name = 'delete_lesson'),
    path('courses_list/<slug:course_slug>/deletelink/<int:link_id>/', views.deleteLink, name = 'delete_link'),
    path('courses_list/<slug:course_slug>/createlink/<int:lesson_id>/', views.create_link, name = 'createlink'),
    path('courses_list/<slug:course_slug>/create/', views.create, name = 'create'),
    path('courses_list/<slug:course_slug>/', views.lessons_list, name = 'lessons_list'),
    path('courses_list/', views.courses_list, name = 'courses_list'),
    path('courses/lessons/<slug:course_slug>/<int:lesson_id>', views.lessons, name = 'lessons'),
    path('courses/', views.courses, name = 'courses'),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('media/pptxfiles/<str:filename>', views.secure_file_read, name = "download"),
    path('availablelesson/<slug:lesson_slug>', views.available_lesson, name = "available_lesson"),
]