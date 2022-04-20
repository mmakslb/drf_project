import pytest


@pytest.fixture
def create_superuser(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_superuser(**kwargs)
    return make_user
