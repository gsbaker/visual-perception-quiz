from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# Create your views here.


class IndexView(generic.ListView):
    paginate_by = 1
    model = Question
    template_name = 'quiz/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('-id')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'quiz/results.html'


def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the answering form
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.save()
        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))

