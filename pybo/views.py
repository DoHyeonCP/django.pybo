from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
    """
    pybo 목록출력
    """
    question_list = Question.objects.all().order_by('-create_date')
    page = request.GET.get('page')
    paginator = Paginator(question_list, 10)
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
        
    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1
        
    rightIndex = (int(page) + 2)
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
        
    custom_range = range(leftIndex, rightIndex + 1)
        
    
    context = {'question_list': question_list, 'page_obj': page_obj, 'paginator': paginator, 'custom_range': custom_range}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html',context)

def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
        else:
            form = AnswerForm()
        context = {'question': question, 'form':form}
        return render(request, 'pybo/question_detail.html', context)
    # question.answer_set.create(content = request.POST.get('content'),
    #                             create_date = timezone.now())
    # return redirect('pybo:detail', question_id = question.id)  

def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST':    #submit을 통한 POST 요청
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit = False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:                           #get 요청
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
