# URLConf for mapping views to urls

from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    # ex: /quiz/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /quiz/questions/
    path('questions/', views.QuestionsView.as_view(), name='questions'),
    path('form/', views.get_name, name='form'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.QuestionFormView.as_view(), name='qa-form'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
]