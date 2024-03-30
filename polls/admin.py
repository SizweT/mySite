# polls/admin.py
from django.contrib import admin
from .models import Question, Choice
from .forms import ChoiceInlineForm


class ChoiceInline(admin.TabularInline):
    model = Choice
    form = ChoiceInlineForm
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
