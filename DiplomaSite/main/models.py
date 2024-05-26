from django.db import models
from django.core.validators import MinValueValidator, FileExtensionValidator, MaxValueValidator
from django_quill.fields import QuillField
from django.template.defaultfilters import truncatechars
import random


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

class CommentsOnLesson(models.Model):
    lesson = models.ForeignKey(AvailableLessons, default=None, blank = False, on_delete=models.CASCADE)
    author = models.CharField('Автор', max_length=50)
    comment = models.TextField('Комментарий', max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    @property
    def short_comment(self):
        return truncatechars(self.comment, 35)


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, default=None, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default = 5)
    
    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs =  list(Answer.objects.filter(question= self))
        data = []
        random.shuffle(answer_objs)
        
        for  answer_obj in answer_objs:
            data.append({
                'answer' :answer_obj.answer, 
                'is_correct' : answer_obj.is_correct
            })
        return data
    
class Answer(models.Model):
    question = models.ForeignKey(Question,related_name='question_answer',  on_delete =models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.answer 