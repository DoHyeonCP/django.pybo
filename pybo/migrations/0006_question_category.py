# Generated by Django 4.2.2 on 2023-11-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('FL', 'Flask'), ('DJ', 'Django'), ('FA', 'FastAPI'), ('BD', 'Big Data'), ('ML', 'Machine learning'), ('WC', 'Web Crawling')], default='FL', max_length=2),
        ),
    ]