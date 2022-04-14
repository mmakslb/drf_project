from rest_framework import serializers, request
from .models import Message, Question
from django.contrib.auth import get_user_model


User = get_user_model()


class QuestionSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Question
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = "__all__"


class QuestionDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'text', 'slug', 'status', 'timestamp', 'sender', 'messages']

