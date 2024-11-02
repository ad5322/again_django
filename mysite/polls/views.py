from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Question,Choice
from django.http import Http404

#index page or home page
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)

#detail page for index page
def detail(request,question_id):
    
    question = get_object_or_404(Question,pk=question_id)
    
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    return HttpResponse(f'you are looking at results of question - {question_id}')

def vote(request,question_id):
    return HttpResponse(f'you are voting on question - {question_id}')