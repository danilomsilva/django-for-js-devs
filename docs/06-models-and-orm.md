# Chapter 6 — Models & ORM

## TL;DR

- A Django model is a Python class that maps to a database table — close in spirit to a Prisma schema, but written in Python instead of Prisma's own DSL.
- QuerySets are **lazy** — writing `Model.objects.filter(...)` doesn't hit the database until you actually consume the result.
- Relations (`ForeignKey`, etc.) work like Prisma relations — Django gives you both directions for free (`greeting.category` and `category.greetings`).

## The mental model

Ok, we've routed a request to a view (chapter 5). Most views need data, and that data lives in the database. Let's look at how Django models that.

```mermaid
flowchart LR
    Model[Python class: Greeting] -->|makemigrations / migrate, ch.7| Table[(Postgres table)]
    Code[Greeting.objects.filter(...)] -->|lazy, builds SQL| Query[QuerySet]
    Query -->|evaluated when consumed| Rows[Rows from Postgres]
```

## If you know JS: Prisma schema + client

```prisma
// schema.prisma
model Greeting {
  id         Int       @id @default(autoincrement())
  message    String
  createdAt  DateTime  @default(now())
  category   GreetingCategory? @relation(fields: [categoryId], references: [id])
  categoryId Int?
}

model GreetingCategory {
  id        Int        @id @default(autoincrement())
  name      String     @unique
  greetings Greeting[]
}
```

```python
# examples/greetings/models.py
class GreetingCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
```

Where Prisma separates the schema (a `.prisma` file) from the client you query with, Django's model class *is* both — the field definitions and the query interface (`Greeting.objects`) live on the same class.

| Prisma | Django ORM |
|---|---|
| `schema.prisma` model block | A `models.Model` subclass |
| `prisma.greeting.findMany()` | `Greeting.objects.all()` |
| `prisma.greeting.findMany({ where: { ... } })` | `Greeting.objects.filter(...)` |
| `include: { category: true }` | `select_related("category")` (chapter 19) |
| `@relation` | `ForeignKey` |
| `prisma migrate dev` | `makemigrations` + `migrate` (chapter 7) |

## The Django way

**Fields describe both the column and the validation.** `CharField(max_length=200)` is a `VARCHAR(200)` column *and* the max-length rule DRF serializers (chapter 11) will enforce automatically.

**Relations are two-way, automatically.** `ForeignKey(GreetingCategory, related_name="greetings")` on `Greeting` gives you:

```python
greeting.category          # forward: the related GreetingCategory instance
category.greetings.all()   # reverse: every Greeting with this category — via related_name
```

You get the reverse accessor for free — in Prisma you'd declare `greetings: Greeting[]` explicitly on the other model; Django derives it from `related_name`.

**QuerySets are lazy.** This is the one that catches people off guard:

```python
qs = Greeting.objects.filter(category__name="Formal")  # no query has run yet
list(qs)          # NOW it runs
for g in qs:       # or this
    ...
```

Django builds up the query as you chain `.filter()`, `.exclude()`, `.order_by()`, etc., and only sends SQL to Postgres when you iterate, call `list()`, index into it, or otherwise force evaluation. This is closer to a lazily-built query object than to Prisma's promise-based `findMany()`, which sends the query as soon as you `await` it — with Django, chaining filters costs nothing until you actually ask for the data.

**`on_delete` is mandatory and explicit.** Every `ForeignKey` must say what happens to a `Greeting` if its `GreetingCategory` is deleted. `SET_NULL` (used here, since `category` is nullable) clears the reference; `CASCADE` would delete the `Greeting` too. There's no silent default — Prisma requires you to think about this too via `onDelete`, but Django surfaces it at the field level every time.

See it working: [`examples/greetings/tests.py`](../examples/greetings/tests.py)'s `test_greeting_category_relation` creates a category, attaches a greeting to it, and checks both directions.

## Gotchas for JS devs

- Forgetting that QuerySets are lazy is a common source of confusion — printing a QuerySet in a debugger *does* evaluate it (Django implements `__repr__` to run a limited query), which can mask the laziness until you hit a case where it matters (e.g. building a queryset conditionally across several `if` branches).
- `related_name` isn't optional in practice — without it, Django auto-generates one (`greeting_set`), which works but is less readable. Always set it explicitly.
- Model methods and properties are regular Python — there's no special "computed field" syntax like some ORMs have; you just write a method or use `@property`.

## Check yourself

1. When does `Greeting.objects.filter(message__startswith="Hello")` actually query the database?

   <details><summary>Answer</summary>Not when it's written — only when the resulting QuerySet is evaluated: iterated, converted to a list, indexed, etc. QuerySets are lazy.</details>

2. Given `category.greetings.all()`, where does `greetings` come from if it's not defined anywhere on `GreetingCategory`?

   <details><summary>Answer</summary>From <code>related_name="greetings"</code> on the <code>ForeignKey</code> field in <code>Greeting</code> — Django adds the reverse accessor to the related model automatically.</details>

## Go deeper (when you need it)

- [Django docs — models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django docs — making queries](https://docs.djangoproject.com/en/5.2/topics/db/queries/)
- [Django docs — QuerySet API](https://docs.djangoproject.com/en/5.2/ref/models/querysets/)

## Further reading & credits

- [Django docs — models](https://docs.djangoproject.com/en/5.2/topics/db/models/) — Django Software Foundation, BSD-3-Clause.
- [Prisma schema reference](https://www.prisma.io/docs/orm/prisma-schema) — Prisma, Apache-2.0.
