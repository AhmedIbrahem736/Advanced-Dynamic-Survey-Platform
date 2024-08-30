from django.db import models
from apps.base.models import CustomBaseModel


class Survey(CustomBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="created_surveys")
