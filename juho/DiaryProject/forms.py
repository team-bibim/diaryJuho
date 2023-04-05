from django import forms
from DiaryProject.models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }