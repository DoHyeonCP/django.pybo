from ..models import Question
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
def index(request):
    """
    pybo 목록출력
    """
    question_list = Question.objects.all().order_by('-create_date')
    page = request.GET.get('page')
    kw = request.GET.get('kw','')#검색어
    category = request.GET.get('category', '')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)

    if category:
        question_list = question_list.filter(category=category)
    
    
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
        
    
    context = {'question_list': question_list, 'page_obj': page_obj, 'paginator': paginator, 'custom_range': custom_range, 'kw': kw, 'category': category}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html',context)