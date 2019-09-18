from django.shortcuts import render
from .serializers import QuizSerializer, OptionSerializer, AnswerSerializer
from rest_framework import generics
from .models import Quiz, Option, Answer
import json

def json_stuff():
    json_file = 'static/data.json'

    with open(json_file) as json_data:
        data = json.load(json_data)
    topics = []
    questions = []
    answers = []
    options = []

    for key, value in data.items():
        for key1, value1 in value.items():
            topics.append(key1)
            for key2, value2 in value1.items():
                for key3, value3 in value2.items():
                    if key3 == 'question':
                        questions.append(value3)
                    elif key3 == 'options':
                        options.append(value3)
                    else:
                        answers.append(value3)
    topics.append('maths')  # one thing I didnt know how to do

    return topics,questions,answers,options

def save_questions():
    topics,questions,answers,options = json_stuff()
    for i in range(0, 3):
        quiz_instance = Quiz.objects.create(question=questions[i])
        quiz_instance.topic = topics[i]
        quiz_instance.save()

def save_options():
    topics,questions,answers,options = json_stuff()
    for i in range(1, 4):
        for op in options:
            for o in op:
                options_instance = Option.objects.get_or_create(question=Quiz(id=i),option=o)

def save_answers():
    topics,questions,answers,options = json_stuff()
    for i in range(1, 4):
        answer_instance = Answer.objects.get_or_create(question=Quiz(id=i),answer=answers[i-1])

class CreateQuizView(generics.ListCreateAPIView):
    "This class creates a serializer "
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class QuizDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class CreateOptionView(generics.ListCreateAPIView):
    "This class creates a serializer "
    serializer_class = OptionSerializer
    queryset = Option.objects.all()


class OptionDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class CreateAnswerView(generics.ListCreateAPIView):
    "This class creates a serializer "
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()



class AnswerDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
