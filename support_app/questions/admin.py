from django.contrib import admin
import nested_admin
from .models import Question, Message


class QuestionInline(admin.TabularInline):
    model = Question


@admin.register(Message)
class MessageAdmin(nested_admin.NestedModelAdmin):
    list_display = ['id', 'question', 'sender', 'text', 'timestamp']


class MessageInline(admin.TabularInline):
    model = Message


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'title', 'status', 'timestamp']
    inlines = [MessageInline, ]
