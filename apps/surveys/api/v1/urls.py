from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.surveys.api.v1.views import SurveyViewSet, SectionViewSet, QuestionViewSet

router = DefaultRouter()

router.register(prefix="survey", viewset=SurveyViewSet, basename="survey-api")
router.register(prefix="section", viewset=SectionViewSet, basename="section-api")
router.register(prefix="question", viewset=QuestionViewSet, basename="question-api")

urlpatterns = [
    path("", include(router.urls)),
]
