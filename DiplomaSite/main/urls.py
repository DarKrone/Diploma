from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('courseslist/<int:courseid>/edit/<int:lessonid>/', views.edit, name = 'edit'),
    path('courseslist/<int:courseid>/delete/<int:lessonid>/', views.delete, name = 'delete'),
    path('courseslist/<int:courseid>/create/', views.create, name = 'create'),
    path('courseslist/<int:courseid>/', views.lessonslist, name = 'lessonslist'),
    path('courseslist/', views.courseslist, name = 'courseslist'),
    path('courses/lessons/<int:courseid>/<int:lessonid>', views.lessons, name = 'lessons'),
    path('courses/', views.courses, name = 'courses')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)