from django.db import transaction

from .models import Greeting, GreetingCategory


class MessageRequiredError(Exception):
    pass


@transaction.atomic
def create_greeting_with_new_category(message: str, category_name: str) -> Greeting:
    """Creates a category and a greeting in it as one unit — if either step
    fails, both are rolled back. Demonstrates transaction.atomic (chapter 20).
    """
    category = GreetingCategory.objects.create(name=category_name)

    if not message.strip():
        # Raised *after* the category insert already ran — atomic() still
        # rolls it back, because nothing in this function has committed yet.
        raise MessageRequiredError("message cannot be blank.")

    return Greeting.objects.create(message=message, category=category)
