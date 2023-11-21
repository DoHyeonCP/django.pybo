from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Question
from ..forms import QuestionForm
from django.utils import timezone

@login_required(login_url='accounts:login')
def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST':    #submit을 통한 POST 요청
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit = False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:                           #get 요청
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url = 'accounts:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id = question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance = question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='accounts:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='accounts:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)