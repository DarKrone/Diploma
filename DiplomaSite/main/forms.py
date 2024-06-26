from .models import Lesson
from django.forms import ModelForm, TextInput, Textarea, Select, ClearableFileInput, NumberInput

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["course","number", "title", "description", "lesson","presentation_file"]
        widgets = {
            "course": Select(attrs={
                'class': 'form-control shadow-sm'
            }),
            "number": NumberInput(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Введите номер занятия',
                'min': 1,
            }),
            "title": TextInput(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Введите название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Введите описание'
            }),
            "presentation_file": ClearableFileInput(attrs={
                'class': 'form-control shadow-sm',
                'accept': '.pdf, .doc, .docx, .xlsx, .xls',
            })
        }