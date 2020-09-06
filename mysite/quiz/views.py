from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import User, Question, Choice, Answer
from .forms import UserForm, QuestionAnswerForm
from .scripts import find_high_score
import logging

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
        self.request.session['user_id'] = user.id

        return HttpResponseRedirect(reverse('quiz:qa-form', args=(1, )))


class QuestionFormView(generic.CreateView):
    form_class = QuestionAnswerForm
    model = Answer
    template_name = 'quiz/question-form.html'

    def get_initial(self):
        initial = super(QuestionFormView, self).get_initial()

        current_question = Question.objects.get(pk=self.kwargs['pk'])
        initial['question'] = Question.objects.get(pk=self.kwargs['pk'])

        # check if the user has already made a choice for this question
        try:
            user_id = self.request.session['user_id']
            selected_id = str(user_id) + "-" + str(current_question.id)
            current_choice_id = self.request.session[selected_id]
            current_choice = Choice.objects.get(pk=current_choice_id)
        except KeyError:
            pass
        else:
            initial['choices'] = current_choice

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_question = Question.objects.get(pk=self.kwargs['pk'])
        context['current_question'] = current_question

        # try and get a previous question
        try:
            prev_id = current_question.id - 1
            prev_question = Question.objects.get(pk=prev_id)
        except (KeyError, Question.DoesNotExist):
            pass
        else:
            context['previous_question'] = prev_question

        # try and get a next question
        try:
            next_id = current_question.id + 1
            next_question = Question.objects.get(pk=next_id)
        except (KeyError, Question.DoesNotExist):
            pass
        else:
            context['next_question'] = next_question

        return context

    def form_invalid(self, form):
        current_question = Question.objects.get(pk=self.kwargs['pk'])
        if 'prev' in self.request.POST:
            prev_question_id = current_question.id - 1
            return HttpResponseRedirect(reverse("quiz:qa-form", args=(prev_question_id,)))

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        current_question = Question.objects.get(pk=self.kwargs['pk'])

        # get the name of submit input
        if 'next' in self.request.POST:
            pass
        elif 'prev' in self.request.POST:
            prev_question_id = current_question.id - 1
            return HttpResponseRedirect(reverse("quiz:qa-form", args=(prev_question_id,)))

        try:
            selected_choice = current_question.choice_set.get(pk=form.cleaned_data['choices'].id)
        except (KeyError, Choice.DoesNotExist):
            return HttpResponseRedirect(reverse("quiz:qa-form", args=(current_question.pk, )))
        else:
            user_id = self.request.session['user_id']
            if selected_choice.correct:
                # check if this choice has already been selected
                try:
                    selected_id = str(user_id) + "-" + str(current_question.id)
                    current_choice_id = self.request.session[selected_id]
                except KeyError:
                    # this hasn't been selected
                    user = User.objects.get(pk=user_id)
                    user.score += 1
                    user.save()
                    # save the selected choice using session data
                    selected_id = str(user_id) + "-" + str(current_question.id)
                    self.request.session[selected_id] = selected_choice.id
                else:
                    pass
            else:
                user = User.objects.get(pk=user_id)
                user.save()
                # save the selected choice using session data
                selected_id = str(user_id) + "-" + str(current_question.id)
                self.request.session[selected_id] = selected_choice.id

        new_question_id = current_question.id + 1
        try:
            Question.objects.get(pk=new_question_id)
        except (KeyError, Question.DoesNotExist):
            user_id = self.request.session['user_id']
            return HttpResponseRedirect(reverse("quiz:results", args=(user_id,)))

        return HttpResponseRedirect(reverse("quiz:qa-form", args=(new_question_id, )))


class ResultsView(generic.DetailView):
    model = User
    template_name = 'quiz/results.html'

    def get_context_data(self, **kwargs):
        current_user = User.objects.get(pk=self.request.session['user_id'])
        users_by_score = User.objects.all().order_by('-score')
        score_list = []
        for user in users_by_score:
            score_list.append(user.score)
        high_score = find_high_score(score_list)
        return {
            "current_user": current_user,
            "users": users_by_score,
            "high_score": high_score
        }
