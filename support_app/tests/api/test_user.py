import pytest


@pytest.mark.django_db
def test_register_and_login_superuser(create_superuser, client):
    create_superuser(username='Admin', password='Admin', email='')
    response = client.post("/auth/jwt/create/", dict(username="Admin", password="Admin"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_and_login_user(create_user, client):
    create_user(username='maksim', password='Testpassword', email='mmakslb@gmail.com')
    response = client.post("/auth/jwt/create/", dict(username="maksim", password="Testpassword"))
    assert response.status_code == 200
