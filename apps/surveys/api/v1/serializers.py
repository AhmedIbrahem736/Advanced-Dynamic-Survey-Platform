from rest_framework.serializers import ModelSerializer
from apps.surveys.models import Survey


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ["name", "description", "start_date", "end_date", "created_by"]


class SurveyReadOnlySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"
