# URLConf for mapping views to urls

from django.urls import path
from . import views

urlpatterns = [
    # ex: /quiz/
    path('', views.index, name='index'),
    # ex: /quiz/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /quiz/1/answer/
    path('<int:question_id>/answer/', views.answer, name='answer')
]