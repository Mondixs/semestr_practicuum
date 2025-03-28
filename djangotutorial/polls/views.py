from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import QuestionSerializer, ChoiceSerializer, StudentSerializer
from .models import Question, Choice, Student


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# ViewSet для модели Question
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# ViewSet для модели Choice
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

# ViewSet для модели Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer