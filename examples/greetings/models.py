from django.db import models


class GreetingCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "greeting categories"

    def __str__(self):
        return self.name


class Greeting(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        GreetingCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="greetings",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.message
