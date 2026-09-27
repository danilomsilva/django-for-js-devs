import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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
    assert response.json()["results"][0]["message"] == "Hello from Django"


@pytest.mark.django_db
def test_greetings_create_endpoint():
    staff = User.objects.create_user(username="staff", password="s3cret", is_staff=True)
    client = APIClient()
    client.force_authenticate(user=staff)

    response = client.post("/api/greetings/", {"message": "New greeting"})

    assert response.status_code == 201
    assert Greeting.objects.count() == 1


@pytest.mark.django_db
def test_greetings_create_endpoint_requires_staff():
    non_staff = User.objects.create_user(username="regular", password="s3cret")
    client = APIClient()
    client.force_authenticate(user=non_staff)

    response = client.post("/api/greetings/", {"message": "New greeting"})

    assert response.status_code == 403
    assert Greeting.objects.count() == 0


@pytest.mark.django_db
def test_greetings_create_endpoint_rejects_blank_message():
    staff = User.objects.create_user(username="staff2", password="s3cret", is_staff=True)
    client = APIClient()
    client.force_authenticate(user=staff)

    response = client.post("/api/greetings/", {"message": "   "})

    assert response.status_code == 400
    assert "message" in response.json()


@pytest.mark.django_db
def test_greeting_category_relation():
    category = GreetingCategory.objects.create(name="Formal")
    greeting = Greeting.objects.create(message="Good day", category=category)

    assert greeting.category.name == "Formal"
    assert category.greetings.first() == greeting


@pytest.mark.django_db
def test_whoami_requires_authentication():
    client = APIClient()

    response = client.get("/api/whoami/")

    assert response.status_code == 403


@pytest.mark.django_db
def test_whoami_with_token():
    user = User.objects.create_user(username="alice", password="s3cret")
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    response = client.get("/api/whoami/")

    assert response.status_code == 200
    assert response.json() == {"username": "alice"}


@pytest.mark.django_db
def test_obtain_token_endpoint():
    User.objects.create_user(username="alice", password="s3cret")
    client = APIClient()

    response = client.post("/api/auth/token/", {"username": "alice", "password": "s3cret"})

    assert response.status_code == 200
    assert "token" in response.json()


@pytest.mark.django_db
def test_greetings_list_is_paginated():
    for i in range(12):
        Greeting.objects.create(message=f"Greeting {i}")
    client = APIClient()

    response = client.get("/api/greetings/")

    data = response.json()
    assert data["count"] == 12
    assert len(data["results"]) == 10
    assert data["next"] is not None


@pytest.mark.django_db
def test_greetings_filter_by_category_name():
    formal = GreetingCategory.objects.create(name="Formal")
    Greeting.objects.create(message="Good day", category=formal)
    Greeting.objects.create(message="Hey")
    client = APIClient()

    response = client.get("/api/greetings/", {"category__name": "Formal"})

    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["message"] == "Good day"


@pytest.mark.django_db
def test_greetings_ordering():
    Greeting.objects.create(message="B")
    Greeting.objects.create(message="A")
    client = APIClient()

    response = client.get("/api/greetings/", {"ordering": "message"})

    messages = [item["message"] for item in response.json()["results"]]
    assert messages == ["A", "B"]


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
