from rest_framework.serializers import (ModelSerializer, HiddenField, CurrentUserDefault,
                                        ValidationError, PrimaryKeyRelatedField)
from apps.surveys.models import Survey, Section, Question, QuestionChoice, SurveyResponse, QuestionAnswer


class SurveySerializer(ModelSerializer):
    created_by = HiddenField(default=CurrentUserDefault())

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


class SurveyResponseSerializer(ModelSerializer):
    respondent = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = SurveyResponse
        fields = ["survey", "respondent"]


class SurveyResponseReadOnlySerializer(ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = "__all__"


class QuestionAnswerSerializer(ModelSerializer):
    question_choices = PrimaryKeyRelatedField(queryset=QuestionChoice.objects.all(), many=True, required=False)

    class Meta:
        model = QuestionAnswer
        fields = ["text_answer", "question", "survey_response", "question_choices"]

    def validate_survey_response(self, survey_response):
        current_user = self.context.get("current_user")

        if current_user != survey_response.respondent:
            raise ValidationError("This survey response does not belong to the current user.")

        return survey_response

    def validate(self, attrs):
        text_answer = attrs.get("text_answer")
        question_choices = attrs.get("question_choices")

        if text_answer and question_choices:
            raise ValidationError("You cannot pick a choice while submitting an answer text.")

        if not (text_answer or question_choices):
            raise ValidationError("You must submit an answer.")

        return attrs


class QuestionAnswerReadOnlySerializer(ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"
