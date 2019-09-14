import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Question, Choice
from .serializers import QuestionS, ChoiceS


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):

#     question = Question.objects.get(pk=question_id)
#     question.pub_date =  question.pub_date.strftime('%Y-%m-%d %H:%M:%S')
#     question_dic = model_to_dict(question)
#     choice_qs = Choice.objects.filter(question=question).all()
#     choice_list = [model_to_dict(obj) for obj in choice_qs]
#     return render(request, 'polls/detail.html', {'question': json.dumps(question_dic), 'choice_list': json.dumps(choice_list)})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


class QuestionV(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionS


class ChoiceV(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceS



