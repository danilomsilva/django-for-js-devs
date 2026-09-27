import { withMermaid } from "vitepress-mermaid-plugin";

export default withMermaid({
  title: "Django for JS Devs",
  description: "Django explained through the JS tools you already know",
  base: "/django-for-js-devs/",
  cleanUrls: true,
  lastUpdated: true,

  // Chapters link to source files in examples/, CREDITS.md, and CLAUDE.md —
  // real files in the repo, just outside docs/, so not VitePress pages.
  ignoreDeadLinks: [/\.\.\/examples\//, /\.\.\/CREDITS/, /\.\.\/CLAUDE/],

  head: [["link", { rel: "icon", href: "/django-for-js-devs/favicon.svg" }]],

  themeConfig: {
    nav: [
      { text: "Start reading", link: "/00-intro" },
      { text: "Cheat sheet", link: "/appendix-cheat-sheet" },
      { text: "GitHub", link: "https://github.com/danilomsilva/django-for-js-devs" },
    ],

    sidebar: [
      {
        text: "Intro",
        items: [{ text: "00 — Intro", link: "/00-intro" }],
      },
      {
        text: "Part 1 — Mindset",
        items: [
          { text: "01 — Python survival kit", link: "/01-python-survival-kit" },
          { text: "02 — Django philosophy", link: "/02-django-philosophy" },
        ],
      },
      {
        text: "Part 2 — Core Django",
        items: [
          { text: "03 — Project anatomy", link: "/03-project-anatomy" },
          { text: "04 — Request lifecycle", link: "/04-request-lifecycle" },
          { text: "05 — URLs & views", link: "/05-urls-and-views" },
          { text: "06 — Models & ORM", link: "/06-models-and-orm" },
          { text: "07 — Migrations", link: "/07-migrations" },
          { text: "08 — Admin", link: "/08-admin" },
          { text: "09 — Settings & environments", link: "/09-settings-and-environments" },
        ],
      },
      {
        text: "Part 3 — APIs for React",
        items: [
          { text: "10 — DRF intro", link: "/10-drf-intro" },
          { text: "11 — Serializers", link: "/11-serializers" },
          { text: "12 — Auth", link: "/12-auth" },
          { text: "13 — Permissions", link: "/13-permissions" },
          { text: "14 — Pagination, filtering, ordering", link: "/14-pagination-filtering-ordering" },
          { text: "15 — Errors & validation", link: "/15-errors-and-validation" },
          { text: "16 — Typed contracts", link: "/16-typed-contracts" },
          { text: "17 — Dev setup React ↔ Django", link: "/17-dev-setup-react-django" },
        ],
      },
      {
        text: "Part 4 — Data & Postgres",
        items: [
          { text: "18 — Postgres with Django", link: "/18-postgres-with-django" },
          { text: "19 — N+1 queries", link: "/19-n-plus-1-queries" },
          { text: "20 — Transactions", link: "/20-transactions" },
        ],
      },
      {
        text: "Part 5 — Quality & ops",
        items: [
          { text: "21 — Testing", link: "/21-testing" },
          { text: "22 — Tooling", link: "/22-tooling" },
          { text: "23 — Background tasks", link: "/23-background-tasks" },
          { text: "24 — Deploy", link: "/24-deploy" },
          { text: "25 — Observability", link: "/25-observability" },
        ],
      },
      {
        text: "Appendix",
        items: [
          { text: "Cheat sheet", link: "/appendix-cheat-sheet" },
          { text: "Glossary", link: "/appendix-glossary" },
          { text: "Resources", link: "/appendix-resources" },
        ],
      },
    ],

    socialLinks: [{ icon: "github", link: "https://github.com/danilomsilva/django-for-js-devs" }],

    search: {
      provider: "local",
    },

    footer: {
      message: "Content licensed under CC BY 4.0 · Code licensed under MIT",
      copyright: "AI-assisted, human-reviewed · Danilo M. Silva",
    },

    editLink: {
      pattern: "https://github.com/danilomsilva/django-for-js-devs/edit/main/docs/:path",
      text: "Suggest an edit on GitHub",
    },
  },

  markdown: {
    theme: { light: "github-light", dark: "github-dark" },
  },
});
