from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.surveys.models import Survey, Section
from apps.surveys.api.v1.serializers import (SurveySerializer, SurveyReadOnlySerializer,
                                             SectionSerializer, SectionReadOnlySerializer)
from apps.surveys.filters import SurveyFilter, SectionFilter


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


class SectionViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Section.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SectionFilter
    search_fields = ["name", "description"]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return SectionReadOnlySerializer

        return SectionSerializer
