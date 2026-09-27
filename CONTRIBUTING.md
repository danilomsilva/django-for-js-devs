# Contributing

Thanks for considering a contribution to Django for JS Devs. This project is small and opinionated on purpose — please read this before opening a PR.

## What kind of contributions are welcome

- Typos, broken links, unclear wording.
- Bug reports/fixes in `examples/` (with a failing test that your fix makes pass).
- Corrections to a factual claim, version number, or a "> ⚠️ Verify:" flag left in a chapter — please include a link to the source you verified against.
- Suggestions for a clearer JS anchor for a concept, backed by a reason (popularity, clarity, accuracy).

For anything larger — a new chapter, restructuring the chapter plan, adding a dependency — please open an issue first to discuss before writing code or prose.

## Style rules

- Follow `docs/_template.md` for chapter structure.
- Keep chapters short (5–10 minutes reading time). Prefer bullets and tables over long paragraphs.
- Every Django code example must live in `examples/`, run, and be covered by a passing test.
- Never copy text verbatim from official docs, books, or articles — paraphrase and link, and add the source to `CREDITS.md` and the chapter's "Further reading & credits."
- Don't reference a specific company, employer, or personal project.
- Mermaid diagrams are welcome for flows and lifecycles, but only when a diagram is clearer than a bullet list — don't add one just for decoration.

## PR checklist

- [ ] One chapter or one scaffold step per PR (no bundling unrelated changes).
- [ ] If you touched `examples/`: `ruff check` and `ruff format --check` pass, and `pytest` passes locally.
- [ ] If you touched `docs/`: the chapter follows the template and links back to any earlier chapter it builds on.
- [ ] Any unverifiable claim is flagged with `> ⚠️ Verify:` rather than stated as fact.
- [ ] New sources are added to `CREDITS.md`.

## Licensing of contributions

By submitting a PR, you agree your contribution is licensed under the same terms as the rest of the project: MIT for code in `examples/`, CC BY 4.0 for content in `docs/` (see `LICENSE` and `LICENSE-CONTENT`).
