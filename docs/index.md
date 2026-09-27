---
layout: home

hero:
  name: "Django for JS Devs"
  text: "Django, explained through the JS tools you already know"
  tagline: A free, open-source guide for React/Node developers picking up Django — no Python-beginner detours.
  actions:
    - theme: brand
      text: Start reading →
      link: /00-intro
    - theme: alt
      text: Cheat sheet
      link: /appendix-cheat-sheet
    - theme: alt
      text: View on GitHub
      link: https://github.com/danilomsilva/django-for-js-devs

features:
  - title: JS anchor for every concept
    details: Every Django idea — models, views, middleware, serializers — is mapped to the closest popular JS equivalent (Prisma, Express, Zod, and more) before going deeper.
  - title: Runnable and tested
    details: Every Django example lives in a single, growing DRF project in examples/, covered by CI — not disconnected snippets.
  - title: Short and scannable
    details: Each chapter is a 5–10 minute read — mental model, side-by-side code, gotchas, and links to go deeper when you need to.
---

## Who this is for

You're comfortable with **React** on the frontend, you've built or worked on **Node.js** backends, and now you need to work with Django — but every Django resource out there assumes you're a Python beginner, a general programming beginner, or a Django dev learning React. This guide assumes none of that. It assumes you already know how to build a web app; it's here to map Django's world onto the one you already have a mental model for.

## How to read it

- Start at [00 — Intro](/00-intro) and follow the chapter order — later chapters build on earlier ones and link back when they do.
- Every Django code example lives in [`examples/`](https://github.com/danilomsilva/django-for-js-devs/tree/main/examples) on GitHub, a single Django + DRF project that grows chapter by chapter.
- Claims about versions or "most popular JS tool" are verified against current sources; anything unverified is flagged inline with `> ⚠️ Verify:` rather than stated as fact.

This content is AI-assisted and human-reviewed. Written content is licensed [CC BY 4.0](https://github.com/danilomsilva/django-for-js-devs/blob/main/LICENSE-CONTENT), code is [MIT](https://github.com/danilomsilva/django-for-js-devs/blob/main/LICENSE).
