from rest_framework import serializers
from .models import Quiz, Option, Answer


class QuizSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Quiz
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
