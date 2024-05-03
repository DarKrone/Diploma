from django.db import models
from django.core.validators import MinValueValidator, FileExtensionValidator, MaxValueValidator
from django_quill.fields import QuillField


class Courses(models.Model):
    course = models.CharField('Название курса', max_length=255)
    slug = models.SlugField(max_length=100)
    description = models.TextField('Описание курса')

    def __str__(self):
        return self.course
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Courses, default = 1, on_delete=models.CASCADE)
    number = models.IntegerField('Номер урока',default = 1, validators=[MinValueValidator(0)])
    title = models.CharField('Название урока', max_length=255)
    description = models.TextField('Короткое описание')
    lesson = QuillField('Занятие', default=None, blank = True)
    
    presentation_file = models.FileField("Файл занятия", default = None, blank = True, upload_to= 'pptxfiles/', validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'xlsx', 'xls'], "Unsupported file format")])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class AvailableLessons(models.Model):
    lesson = models.ForeignKey(Lesson, default=None, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    link = models.URLField('Ссылка', default = "http://127.0.0.1:8000/availablelesson/", max_length=250)
    password = models.CharField('Пароль к уроку', max_length=100)
    is_active = models.BooleanField('Доступность без пароля', default=False)

    def __str__(self):
        return self.lesson.title
    
    class Meta:
        verbose_name = 'Доступный урок'
        verbose_name_plural = 'Доступные уроки'