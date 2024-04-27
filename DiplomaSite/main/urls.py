from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('courses_list/<int:course_id>/edit/<int:lesson_id>/', views.edit, name = 'edit'),
    path('courses_list/<int:course_id>/delete/<int:lesson_id>/', views.delete, name = 'delete'),
    path('courses_list/<int:course_id>/create/', views.create, name = 'create'),
    path('courses_list/<int:course_id>/', views.lessons_list, name = 'lessons_list'),
    path('courses_list/', views.courses_list, name = 'courses_list'),
    path('courses/lessons/<int:course_id>/<int:lesson_id>', views.lessons, name = 'lessons'),
    path('courses/', views.courses, name = 'courses'),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('media/pptxfiles/<str:filename>', views.secure_file_read, name = "download"),
]