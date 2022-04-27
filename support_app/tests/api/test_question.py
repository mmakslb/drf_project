import pytest


@pytest.mark.django_db
def test_create_question(create_superuser, client):
    create_superuser(
        username='Admin',
        password='Admin',
        email=''
    )

    response = client.post(
        "/auth/jwt/create/",
        dict(
            username="Admin",
            password="Admin"
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
