from rest_framework import serializers
from .models import Question, Choice, Student

# Сериализатор для модели Question
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']

# Сериализатор для модели Choice
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']

# Сериализатор для модели Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'gender', 'age', 'city', 'academic_pressure', 'study_satisfaction']