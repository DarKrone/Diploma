from .models import Lesson
from django.forms import ModelForm, TextInput, Textarea, FileField, Select

 
class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["course","number", "title", "description","presentation_file"]
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер занятия'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
        })
        }