# URLConf for mapping views to urls

from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    # ex: /quiz/
    path('', views.index, name='index'),
    # ex: /quiz/1/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /quiz/1/answer/
    path('<int:question_id>/answer/', views.answer, name='answer')
]