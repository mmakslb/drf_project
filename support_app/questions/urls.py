from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'questions/main', views.QuestionViewSet, basename='questions')
router.register(r'questions/solved', views.SolvedViewSet, basename='solved_questions')
router.register(r'questions/frozen', views.FrozenViewSet, basename='frozen_questions')


urlpatterns = [
    path('', include(router.urls)),

]


