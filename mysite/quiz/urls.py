# URLConf for mapping views to urls

from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    # ex: /quiz/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /quiz/questions/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.QuestionFormView.as_view(), name='question_form'),
    path('continue/', views.InfoView.as_view(), name='info_view'),
    path('results/<int:pk>/', views.ResultsView.as_view(), name='results'),
]