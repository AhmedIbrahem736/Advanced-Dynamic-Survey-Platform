from rest_framework.serializers import ModelSerializer
from apps.surveys.models import Survey, Section, Question, QuestionChoice


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ["name", "description", "start_date", "end_date", "created_by"]


class SurveyReadOnlySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ["name", "description", "survey"]


class SectionReadOnlySerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ["text", "order", "type", "section"]


class QuestionReadOnlySerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionChoiceSerializer(ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ["choice", "question"]


class QuestionChoiceReadOnlySerializer(ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = "__all__"
