import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_and_login_superuser(create_superuser):
    create_superuser(username='maksim', password='Testpassword', email='mmakslb@gmail.com')
    response = client.post("/auth/jwt/create/", dict(username="maksim", password="Testpassword"))
    data = response.data
    print(data['access'])
    assert response.status_code == 200
