from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    CATEGORY_CHOICES = [
        ('파이썬', 'Python'),
        ('웹 개발', "Web Development"),
        ('자동화 및 스크립팅', "Automation and Scripting"),
        ('크롤링', "Web Crawling"),
        ('데이터 분석', "Data Analysis"),
        ('시각화', 'Visualization'),
        ('머신러닝', "Machine learning"),
        ('잡담', 'anything')
        
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES, default = '웹 개발')
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    @staticmethod
    def get_category_questions(category_code):
        return Question.objects.filter(category = category_code)


    def __str__(self):
        return f'{self.subject}'

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    

    def __str__(self):
        return self.subject