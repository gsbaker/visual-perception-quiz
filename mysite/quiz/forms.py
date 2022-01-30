from django import forms
from django.forms import ModelForm
from .models import User, Answer


class UserForm(forms.Form):
    def create_user(self):
        user = User()
        user.save()
        return user


class QuestionAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['choices']

    def __init__(self, *args, **kwargs):
        super(QuestionAnswerForm, self).__init__(*args, **kwargs)
        question = self.initial['question']
        choices_set = question.choice_set.order_by('choice_text')
        self.fields['choices'] = forms.ModelChoiceField(queryset=choices_set,
                                                        widget=forms.RadioSelect,
                                                        label="", )
