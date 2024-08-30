from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.surveys.models import Survey, Section, Question, QuestionChoice, SurveyResponse, QuestionAnswer
from apps.surveys.api.v1.serializers import (SurveySerializer, SurveyReadOnlySerializer,
                                             SectionSerializer, SectionReadOnlySerializer,
                                             QuestionSerializer, QuestionReadOnlySerializer,
                                             QuestionChoiceSerializer, QuestionChoiceReadOnlySerializer,
                                             SurveyResponseSerializer, SurveyResponseReadOnlySerializer,
                                             QuestionAnswerSerializer, QuestionAnswerReadOnlySerializer)
from apps.surveys.filters import (SurveyFilter, SectionFilter, QuestionFilter, QuestionChoiceFilter,
                                  SurveyResponseFilter, QuestionAnswerFilter)


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


class QuestionViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = QuestionFilter
    search_fields = ["text"]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return QuestionReadOnlySerializer

        return QuestionSerializer


class QuestionChoiceViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = QuestionChoice.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = QuestionChoiceFilter
    search_fields = ["choice"]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return QuestionChoiceReadOnlySerializer

        return QuestionChoiceSerializer


class SurveyResponseViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = SurveyResponse.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SurveyResponseFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return SurveyResponseReadOnlySerializer

        return SurveyResponseSerializer


class QuestionAnswerViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = QuestionAnswer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuestionAnswerFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return QuestionAnswerReadOnlySerializer

        return QuestionAnswerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_user'] = self.request.user

        return context
