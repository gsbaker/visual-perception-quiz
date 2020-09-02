from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import User, Question, Choice, Answer
from .forms import UserForm, QuestionAnswerForm

# Create your views here.


class IndexView(generic.FormView):
    form_class = UserForm
    model = User
    template_name = 'quiz/index.html'
    context_object_name = 'user'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.create_user()
        self.request.session['user_name'] = user.name

        return HttpResponseRedirect(reverse('quiz:questions'))


class QuestionsView(generic.ListView):
    template_name = 'quiz/questions.html'
    context_object_name = 'questions_list'
    model = Question

    def get_queryset(self):
        return Question.objects.order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            "user_name": self.request.session['user_name'],
            "question_list": Question.objects.order_by('-id')
        }


class LeaderBoardView(generic.ListView):
    pass


class DetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/detail.html'

    def get_context_data(self, **kwargs):
        return {
            'form': QuestionAnswerForm
        }


class QuestionFormView(generic.CreateView):
    form_class = QuestionAnswerForm
    model = Answer
    template_name = 'quiz/question-form.html'

    def get_initial(self):
        initial = super(QuestionFormView, self).get_initial()
        initial['question'] = Question.objects.get(pk=self.kwargs['pk'])
        return initial



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'quiz/results.html'


def get_name(request):
    # if POST request, process the form data
    if request.method == 'POST':
        # create form instance and populate it with data from the request
        form = UserForm(request.POST)
        # check validity
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to new url
            return HttpResponseRedirect('/thanks/')

    # if GET, create blank form
    else:
        form = UserForm()

    return render(request, 'quiz/form.html', {'form': form})


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

