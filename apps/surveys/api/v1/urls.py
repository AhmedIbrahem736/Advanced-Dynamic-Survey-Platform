from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.surveys.api.v1.views import SurveyViewSet

router = DefaultRouter()

router.register(prefix="survey", viewset=SurveyViewSet, basename="survey-api")

urlpatterns = [
    path("", include(router.urls)),
]
