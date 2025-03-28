from django.urls import include, path

from . import views

from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, ChoiceViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'choices', ChoiceViewSet, basename='choice')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]