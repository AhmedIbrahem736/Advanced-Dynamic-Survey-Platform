from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.surveys.models import Survey
from apps.surveys.api.v1.serializers import SurveySerializer, SurveyReadOnlySerializer
from apps.surveys.filters import SurveyFilter


class SurveyViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Survey.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SurveyFilter
    search_fields = ["name", "description"]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return SurveyReadOnlySerializer

        return SurveySerializer
