import pytest
from rest_framework.test import APIClient

from .models import Greeting, GreetingCategory


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


@pytest.mark.django_db
def test_greeting_category_relation():
    category = GreetingCategory.objects.create(name="Formal")
    greeting = Greeting.objects.create(message="Good day", category=category)

    assert greeting.category.name == "Formal"
    assert category.greetings.first() == greeting


def test_ping_endpoint():
    client = APIClient()

    response = client.get("/api/ping/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.django_db
def test_timing_middleware_adds_header():
    client = APIClient()

    response = client.get("/api/greetings/")

    assert "X-Response-Time-Ms" in response
