import pytest


@pytest.mark.django_db
def test_create_answer(create_superuser, create_user, client):
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
    auth_token_superuser = data['access']

    create_user(
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

    auth_token_user = response.data['access']
    data_question = {"title": "Question1", "text": "T3xt1"}
    response = client.post(
        "/questions/main/",
        data_question,
        HTTP_AUTHORIZATION=f'Bearer {auth_token_user}',
        format='json'
    )

    question_id = response.data['id']
    data_message = {"title": "Admin's Answer", "text": "Admin's ANSWER"}
    response = client.post(
        f'/questions/main/{question_id}/',
        data_message,
        HTTP_AUTHORIZATION=f'Bearer {auth_token_superuser}',
        format='json'
    )
    assert response.status_code == 201

    data_message = {"title": "User's Answer", "text": "User's ANSWER"}
    response = client.post(
        f'/questions/main/{question_id}/',
        data_message,
        HTTP_AUTHORIZATION=f'Bearer {auth_token_user}',
        format='json'
    )
    assert response.status_code == 201
