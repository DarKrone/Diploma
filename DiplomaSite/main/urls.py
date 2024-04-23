from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view(), name = 'home'),
    path('courses/<slug:slug>/', views.Lessons.as_view(), name = 'lessons'),
    path('courses/', views.Course.as_view(), name = 'courses'),
    path('allcourses/', views.AllCourses.as_view(), name = "allcourses"),
    path('allcourses/create/', views.CreateLessonView.as_view(), name = "createlesson"),
    path('allcourses/<int:id>/', views.UpdateLessonView.as_view(), name = "updatelesson"),
    path('allcourses/<int:id>/delete', views.DeleteLessonView.as_view(), name = "deletelesson"),
    path('allcourses/<slug:slug>/', views.AllLessonsOfCourse.as_view(), name = "alllessonsofcourse"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)