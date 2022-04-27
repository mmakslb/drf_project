import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def create_superuser(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_superuser(**kwargs)
    return make_user


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user
