from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice, User
from .forms import UserForm

# Create your views here.


class IndexView(generic.FormView):
    form_class = UserForm
    model = User
    template_name = 'quiz/user-new.html'
    context_object_name = 'user'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.create_user()
        return HttpResponseRedirect(reverse('quiz:questions'))

    def get_queryset(self):
        return User.objects.order_by(id)


class QuestionsView(generic.ListView):
    template_name = 'quiz/questions.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('-id')


class LeaderBoardView(generic.ListView):
    pass


class DetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/detail.html'


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

