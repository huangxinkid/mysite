from rest_framework import serializers

from .models import Question, Choice


class QuestionS(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceS(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
