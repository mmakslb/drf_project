import pytest


@pytest.mark.django_db
def test_update_status(create_superuser, create_user, client):

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

    data_message = {"status": "frozen"}
    response = client.patch(
        f'/questions/main/{question_id}/',
        data_message,
        HTTP_AUTHORIZATION=f'Bearer {auth_token_user}',
        format='json'
    )
    assert response.status_code == 403
