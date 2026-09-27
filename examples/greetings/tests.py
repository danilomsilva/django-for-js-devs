import pytest
from rest_framework.test import APIClient

from .models import Greeting


@pytest.mark.django_db
def test_greeting_str():
    greeting = Greeting.objects.create(message="Hello from Django")
    assert str(greeting) == "Hello from Django"


@pytest.mark.django_db
def test_greetings_list_endpoint():
    Greeting.objects.create(message="Hello from Django")
    client = APIClient()

    response = client.get("/api/greetings/")

    assert response.status_code == 200
    assert response.json()[0]["message"] == "Hello from Django"


@pytest.mark.django_db
def test_greetings_create_endpoint():
    client = APIClient()

    response = client.post("/api/greetings/", {"message": "New greeting"})

    assert response.status_code == 201
    assert Greeting.objects.count() == 1
