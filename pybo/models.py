from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    CATEGORY_CHOICES = [
        ('FL', "Flask"),
        ('DJ', "Django"),
        ('FA', "FastAPI"),
        ('BD', "Big Data"),
        ('ML', "Machine learning"),
        ('WC', "Web Crawling")
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    category = models.CharField(max_length = 2, choices = CATEGORY_CHOICES, default = 'FL')
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