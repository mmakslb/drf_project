from rest_framework import viewsets, permissions, status
from django.db.models import Q
from .tasks import send_email_message
from django.http.response import JsonResponse
from .models import Question
from .serializers import MessageSerializer, QuestionSerializer, QuestionDetailSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.action == 'partial_update' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            queryset = Question.objects.all()
        elif self.request.user.is_authenticated:
            queryset = Question.objects.filter(sender=self.request.user, status='actual')
            query = self.request.GET.get("q")
            if query:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query)
                ).distinct()
        return queryset

    serializer_action_classes = {
        'retrieve': QuestionDetailSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.data.update({'sender': self.request.user})
        return super(QuestionViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs['pk'])
        request.data.update({'sender': question.sender, 'title': question.title, 'text': question.text})
        if question.status != request.data['status']:
            send_email_message.delay(question.sender.email, question.title, request.data["status"])
        return super(QuestionViewSet, self).partial_update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs['pk'])
        request.data.update({'sender': self.request.user, 'question': question.id})
        data = request.data
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=400)


class SolvedViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.action == 'partial_update' or self.action == 'update' or self.action == 'destroy'\
                or self.action == 'create':

            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset = Question.objects.filter(status='solved')
            query = self.request.GET.get("q")
            if query:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query)
                ).distinct()
        return queryset

    serializer_action_classes = {
        'retrieve': QuestionDetailSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

    def partial_update(self, request, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs['pk'])
        request.data.update({'sender': question.sender, 'title': question.title, 'text': question.text})
        if question.status != request.data['status']:
            send_email_message.delay(question.sender.email, question.title, request.data["status"])
        return super(SolvedViewSet, self).partial_update(request, *args, **kwargs)


class FrozenViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.action == 'partial_update' or self.action == 'update' or self.action == 'destroy'\
                or self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            queryset = Question.objects.filter(status='frozen')

        elif self.request.user.is_authenticated:
            queryset = Question.objects.filter(sender=self.request.user, status='frozen')
            query = self.request.GET.get("q")
            if query:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query)
                ).distinct()
        return queryset

    serializer_action_classes = {
        'retrieve': QuestionDetailSerializer,
    }

    def partial_update(self, request, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs['pk'])
        request.data.update({'sender': question.sender, 'title': question.title, 'text': question.text})
        if question.status != request.data['status']:
            send_email_message.delay(question.sender.email, question.title, request.data["status"])
        return super(FrozenViewSet, self).partial_update(request, *args, **kwargs)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

