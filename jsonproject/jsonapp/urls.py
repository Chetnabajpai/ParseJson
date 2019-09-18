from django.urls import path
from .views import *

urlpatterns = [
    path(r'save-questions/', CreateQuizView.as_view(), name="create_q"),
    path(r'question-details/<int:pk>/', QuizDetailsView.as_view(),
         name="details_q"),
    path(r'save-options/', CreateOptionView.as_view(), name="create_o"),
    path(r'option-details/<int:pk>/', OptionDetailsView.as_view(),
         name="details_o"),
    path(r'save-answers/', CreateAnswerView.as_view(), name="answer_o"),
    path(r'answer-details/<int:pk>/',  AnswerDetailsView.as_view(),
         name="details_a"),
]
