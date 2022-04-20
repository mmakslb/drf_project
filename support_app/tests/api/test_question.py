import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_create_question(create_superuser):
    create_superuser(
        username='maksim',
        password='Testpassword',
        email='mmakslb@gmail.com'
    )

    response = client.post(
        "/auth/jwt/create/",
        dict(
            username="maksim",
            password="Testpassword"
        )
    )

    data = response.data
    auth_token = data['access']
    data = {"title": "Question1", "text": "T3xt1"}
    response = client.post(
        "/questions/main/",
        data,
        HTTP_AUTHORIZATION=f'Bearer {auth_token}',
        format='json'
    )
    assert response.status_code == 201
