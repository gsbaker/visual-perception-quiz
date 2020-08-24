from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.


def index(request):
    question_list = Question.objects.order_by("-question_text")
    context = {"question_list": question_list}
    return render(request, "quiz/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "quiz/detail.html", {"question": question})


def answer(request, question_id):
    return HttpResponse("You're answering question %s." % question_id)
