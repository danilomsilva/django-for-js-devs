# CLAUDE.md — standing rules for this repo

This file keeps AI-assisted sessions on track for the "Django for JS Devs" guide. Read `0-initiative.md` (scope) and `1-writing-plan.md` (sequencing) first — this file is about *how* to work, not *what* to build.

## Non-negotiables

- **Verify, don't recall.** Any claim about a Django/DRF/Python version, API, or "most popular JS tool" must be checked against a current official source (docs site, package registry, current survey data) before it goes into a chapter. If you can't verify something, write `> ⚠️ Verify:` inline instead of guessing.
- **Runnable and tested.** Every Django code example that lives in `examples/` must run and be covered by a passing test in CI. JS snippets in `docs/` are illustrative and don't need to run, but must not be misleading.
- **No verbatim copying.** Never paste text from Django docs, DRF docs, books, or articles. Paraphrase, explain in your own words, and link to the source. Credit in `CREDITS.md` and in the chapter's "Further reading & credits" section.
- **One chapter or scaffold step per PR.** Don't bundle multiple chapters or unrelated scaffold changes into one PR.
- **Ask before:** adding a new dependency, changing the chapter plan/order, starting the capstone, or deviating from the JS-anchor table in `0-initiative.md`.
- **Never mention** a specific company, employer, or the author's personal projects/work history in any chapter content.
- **✅ before ⏳.** Don't write a "later" chapter while a "core" chapter is still unwritten, unless explicitly told to.

## Copyright and licensing — staying safe

- Written content is CC BY 4.0, code is MIT. Both must be stated in `README.md` and license files, and kept consistent.
- Base explanations on **public, free, and open-source sources**: official Django/DRF docs (BSD-licensed projects, docs generally freely redistributable with attribution — still paraphrase, don't copy), project READMEs, official blogs, and open-source community talks/articles that are freely accessible without a paywall.
- Avoid sourcing from paid books, paywalled tutorials, or proprietary training material — even for background research. If a fact can only be confirmed via a paywalled source, look for an official/free equivalent instead of citing the paywalled one.
- Diagrams, code samples, and explanations should be written fresh, not adapted line-by-line from someone else's diagram or snippet. Structural inspiration is fine (e.g. "middleware pipeline" as a concept); copying someone's exact example verbatim is not.
- When in doubt about whether something is "close enough" to a source to be a problem, don't ship it — rewrite it more independently or drop the reference and just link out.

## Writing style

- Follow the chapter template in `docs/_template.md` exactly — TL;DR, mental model, "If you know JS," "The Django way," gotchas, check-yourself, go deeper, further reading & credits.
- Keep chapters scannable: bullets and tables over prose paragraphs, side-by-side code blocks for JS vs. Django comparisons.
- Aim for 5–10 minutes reading time per chapter. If a chapter is running long, split depth out into a linked "go deeper" reference instead of inlining it.
- **Mermaid diagrams are welcome and encouraged** wherever a flow, request lifecycle, or relationship between pieces (e.g. middleware → URLs → view → response) is easier to grasp visually than in prose — but only when they clarify, not when they add ceremony to something simple enough for a bullet list or one-line description. Don't force a diagram into a chapter that doesn't need one.

## Publishing (later, not now)

- A GitHub Pages site (the "book" itself, easy to read online) is planned — but **only after all chapters are complete**, not during active writing. Don't scaffold GH Pages, a docs site generator (VitePress or otherwise), or any publish workflow until the author explicitly says the guide is done and asks for it.
- Until then, the repo's Markdown files in `docs/` are the only reading surface.

## When starting a new chapter

1. Confirm it's next in `1-writing-plan.md` sequencing (✅ before ⏳, in order, unless told otherwise).
2. Check the current stable versions of anything version-sensitive before writing.
3. Write the runnable example in `examples/` first (or extend the existing one), get it passing under CI, then write the chapter referencing it.
4. Draft the chapter, flag unverifiable claims, list credits.
5. Stop for author review before merging — don't self-merge multiple chapters in a row.
