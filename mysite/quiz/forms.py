from django import forms
from django.forms import ModelForm
from .models import User, QuestionChoices


class UserForm(forms.Form):
    def create_user(self):
        user = User()
        user.save()
        return user


class QuestionChoiceForm(ModelForm):
    class Meta:
        model = QuestionChoices
        fields = ['choices']

    def __init__(self, *args, **kwargs):
        super(QuestionChoiceForm, self).__init__(*args, **kwargs)
        question = self.initial['question']
        choices_set = question.choice_set.order_by('choice_text')
        self.fields['choices'] = forms.ModelChoiceField(queryset=choices_set,
                                                        widget=forms.RadioSelect,
                                                        label="", )
