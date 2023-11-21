from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'category', 'content']


        labels = {
            'subject': '제목',
            'content': '내용'
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }