from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import QuestionAnswerForm, UserForm
from .models import User, Question, Choice, Answer, IncorrectChoice


# Create your views here.


class IndexView(generic.FormView):
    form_class = UserForm
    template_name = 'quiz/index.html'
    context_object_name = 'user'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.create_user()

        if not user:  # check_user returned False
            return HttpResponseRedirect(reverse('quiz:index'))

        self.request.session['user_id'] = user.id

        return HttpResponseRedirect(reverse('quiz:question_form', args=(1,)))


class QuestionFormView(generic.CreateView):
    form_class = QuestionAnswerForm
    model = Answer
    template_name = 'quiz/detail.html'

    def get_initial(self):
        initial = super(QuestionFormView, self).get_initial()
        initial['question'] = self.get_current_question()
        if self.prev_choice_selection_exists():
            user_id = self.request.session['user_id']
            selected_id = str(user_id) + "-" + str(self.get_current_question().id)
            current_choice_id = self.request.session[selected_id]
            current_choice = Choice.objects.get(pk=current_choice_id)
            initial['choices'] = current_choice
        return initial

    def get_current_question(self, **kwargs):
        return Question.objects.get(pk=self.kwargs['pk'])

    def get_current_user(self):
        return User.objects.get(pk=self.request.session['user_id'])

    def get_image_path(self):
        current_question_id = self.get_current_question().id
        if current_question_id <= 20:
            image_index = current_question_id
        elif current_question_id <= 30:
            image_index = current_question_id - 10
        else:
            image_index = current_question_id - 20
        return "quiz/lines/lines-" + str(image_index) + ".jpg"

    def get_sorted_choices_set(self):
        choices_set = self.get_current_question().choice_set.all()
        return sorted(choices_set, key=lambda x: x.choice_text[-1])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_question'] = self.get_current_question()
        context['image_path'] = self.get_image_path()
        context['sorted_choices_set'] = self.get_sorted_choices_set()
        return context

    def form_invalid(self, form):
        print("form_invalid being called")
        if 'prev' in self.request.POST:
            prev_question_id = self.get_current_question().id - 1
            return HttpResponseRedirect(reverse("quiz:question_form", args=(prev_question_id,)))

    def get_selected_choice(self, form):
        try:
            selected_choice = self.get_current_question().choice_set.get(pk=form.cleaned_data['choices'].id)
            return selected_choice
        except (KeyError, Choice.DoesNotExist):
            return HttpResponseRedirect(reverse("quiz:question_form", args=(self.get_current_question().pk,)))

    def prev_choice_selection_exists(self):
        try:
            user_choice_key = str(self.get_current_user().id) + "-" + str(self.get_current_question().id)
            previous_choice = self.get_current_question().choice_set.get(pk=self.request.session[user_choice_key])
            if previous_choice:
                return True
        except (KeyError, Choice.DoesNotExist):
            return False

    def save_choice(self, choice):
        user_choice_key = str(self.get_current_user().id) + "-" + str(self.get_current_question().id)
        self.request.session[user_choice_key] = choice.id
        self.get_current_user().save()

    def get_new_question(self):
        new_question_id = self.get_current_question().id + 1
        try:
            Question.objects.get(pk=new_question_id)
        except (KeyError, Question.DoesNotExist):
            # user_id = self.request.session['user_id']
            return HttpResponseRedirect(reverse("quiz:complete"))

        if self.get_current_question().id % 10 == 0:
            self.request.session['current_question'] = self.get_current_question().id
            return HttpResponseRedirect(reverse("quiz:info_view"))

        return HttpResponseRedirect(reverse("quiz:question_form", args=(new_question_id,)))

    def save_incorrect_choice(self, choice):
        incorrect_choice = IncorrectChoice()
        incorrect_choice.question = self.get_current_question()
        incorrect_choice.choice = choice
        incorrect_choice.user = self.get_current_user()
        incorrect_choice.save()

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if self.prev_choice_selection_exists():
            self.get_new_question()
        # get selected choice
        selected_choice = self.get_selected_choice(form)
        # check for an incorrect answer
        if not selected_choice.correct:
            self.save_incorrect_choice(selected_choice)
        # save the selected choice
        self.save_choice(selected_choice)
        return self.get_new_question()


class InfoView(generic.TemplateView):
    template_name = 'quiz/info.html'

    def get_context_data(self, **kwargs):
        current_question_id = self.request.session['current_question']
        current_section = int(current_question_id / 10)
        next_question_id = current_question_id + 1
        return {
            "current_section": current_section,
            "next_question_id": next_question_id,
        }


class CompleteView(generic.TemplateView):
    template_name = 'quiz/complete.html'
