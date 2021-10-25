from django import forms
from django.forms import ModelForm
from .models import User, Answer
from .scripts import check_user


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label="", widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'id': 'nameInput',
                'name': 'nameInput',
                'class': 'form-control'
            }))

    def create_user(self):
        user = User()
        user.name = self.cleaned_data['name']
        existing_users = User.objects.all()
        if check_user(user, existing_users):
            user.save()
            return user
        return False


class QuestionAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['choices']

    def __init__(self, *args, **kwargs):
        super(QuestionAnswerForm, self).__init__(*args, **kwargs)
        question = self.initial['question']
        self.fields['choices'] = forms.ModelChoiceField(queryset=question.choice_set.all(),
                                                        widget=forms.RadioSelect,
                                                        label="", )