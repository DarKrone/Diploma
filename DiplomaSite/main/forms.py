from .models import Lesson
from django.forms import ModelForm, TextInput, Textarea, Select, ClearableFileInput

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["course","number", "title", "description","presentation_file"]
        widgets = {
            "course": Select(attrs={
                'class': 'form-control'
            }),
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
            }),
            "presentation_file": ClearableFileInput(attrs={
                'class': 'form-control',
            })
        }