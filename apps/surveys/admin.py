from django.contrib import admin
from apps.surveys.models import Survey, Section, Question, QuestionChoice


admin.site.register(Survey)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(QuestionChoice)
