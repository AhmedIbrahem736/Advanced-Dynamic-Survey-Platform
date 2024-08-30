from django.db import models
from apps.base.models import CustomBaseModel


class QuestionType(models.TextChoices):
    TEXT = "text"
    NUMBER = "number"
    DATE = "date"
    DROPDOWN = "dropdown"
    CHECKBOX = "checkbox"
    RADIO_BUTTON = "radio button"


class Question(CustomBaseModel):
    text = models.TextField()
    order = models.PositiveIntegerField()
    type = models.CharField(max_length=50, choices=QuestionType.choices, default=QuestionType.TEXT)
    section = models.ForeignKey("surveys.Section", on_delete=models.CASCADE, related_name="questions")
