---
name: playwright-core
description: Battle-tested Playwright patterns for E2E, API, component, visual, accessibility,
  and security testing. Covers locators, assertions, fixtures, network mocking, auth
  flows, debugging, and framework re…
source_repo: zebbern/claude-code-guide
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Playwright Core Testing

> Opinionated, production-tested Playwright guidance — every pattern includes when (and when _not_) to use it.

**46 reference guides** covering the full Playwright testing surface: selectors, assertions, fixtures, network mocking, auth, visual regression, accessibility, API testing, debugging, and more — with TypeScript and JavaScript examples throughout.

## Golden Rules

1. **`getByRole()` over CSS/XPath** — resilient to markup changes, mirrors how users see the page
2. **Never `page.waitForTimeout()`** — use `expect(locator).toBeVisible()` or `page.waitForURL()`
3. **Web-first assertions** — `expect(locator)` auto-retries; `expect(await locator.textContent())` does not
4. **Isolate every test** — no shared state, no execution-order dependencies
5. **`baseURL` in config** — zero hardcoded URLs in tests
6. **Retries: `2` in CI, `0` locally** — surface flakiness where it matters
7. **Traces: `'on-first-retry'`** — rich debugging artifacts without CI slowdown
8. **Fixtures over globals** — share state via `test.extend()`, not module-level variables
9. **One behavior per test** — multiple related `expect()` calls are fine
10. **Mock external services only** — never mock your own app; mock third-party APIs, payment gateways, email

## Guide Index

### Writing Tests

| What you're doing          | Guide                                                  | Deep dive                                          |
| -------------------------- | ------------------------------------------------------ | -------------------------------------------------- |
| Choosing selectors         | [locators.md                             | [locator-strategy.md         |
| Assertions & waiting       | [assertions-and-waiting.md |                                                    |
| Organizing test suites     | [test-organization.md           | [test-architecture.md       |
| Playwright config          | [configuration.md                   |                                                    |
| Fixtures & hooks           | [fixtures-and-hooks.md         |                                                    |
| Test data                  | [test-data-management.md     |                                                    |
| Auth & login               | [authentication.md                 | [auth-flows.md                     |
| API testing (REST/GraphQL) | [api-testing.md                       |                                                    |
| Visual regression          | [visual-regression.md           |                                                    |
| Accessibility              | [accessibility.md                   |                                                    |
| Mobile & responsive        | [mobile-and-responsive.md   |                                                    |
| Component testing          | [component-testing.md           |                                                    |
| Network mocking            | [network-mocking.md               | [when-to-mock.md                 |
| Forms & validation         | [forms-and-validation.md     |                                                    |
| File uploads/downloads     | [file-operations.md               | [file-upload-download.md |
| Error & edge cases         | [error-and-edge-cases.md     |                                                    |
| CRUD flows                 | [crud-testing.md                     |                                                    |
| Drag and drop              | [drag-and-drop.md                   |                                                    |
| Search & filter UI         | [search-and-filter.md           |                                                    |

### Debugging & Fixing

| Problem                    | Guide                                    |
| -------------------------- | ---------------------------------------- |
| General debugging workflow | [debugging.md             |
| Specific error message     | [error-index.md         |
| Flaky / intermittent tests | [flaky-tests.md         |
| Common beginner mistakes   | [common-pitfalls.md |

### Framework Recipes

| Framework                           | Guide                    |
| ----------------------------------- | ------------------------ |
| Next.js (App Router + Pages Router) | [nextjs.md   |
| React (CRA, Vite)                   | [react.md     |
| Vue 3 / Nuxt                        | [vue.md         |
| Angular                             | [angular.md |

### Specialized Topics

| Topic                                      | Guide                                                              |
| ------------------------------------------ | ------------------------------------------------------------------ |
| Multi-user & collaboration                 | [multi-user-and-collaboration.md |
| WebSockets & real-time                     | [websockets-and-realtime.md           |
| Browser APIs (geo, clipboard, permissions) | [browser-apis.md                                 |
| iframes & Shadow DOM                       | [iframes-and-shadow-dom.md             |
| Canvas & WebGL                             | [canvas-and-webgl.md                         |
| Service workers & PWA                      | [service-workers-and-pwa.md           |
| Electron apps                              | [electron-testing.md                         |
| Browser extensions                         | [browser-extensions.md                     |
| Security testing                           | [security-testing.md                         |
| Performance & benchmarks                   | [performance-testing.md                   |
| i18n & localization                        | [i18n-and-localization.md               |
| Multi-tab & popups                         | [multi-context-and-popups.md         |
| Clock & time mocking                       | [clock-and-time-mocking.md             |
| Third-party integrations                   | [third-party-integrations.md         |

### Architecture Decisions

| Question                 | Guide                                        |
| ------------------------ | -------------------------------------------- |
| Which locator strategy?  | [locator-strategy.md   |
| E2E vs component vs API? | [test-architecture.md |
| Mock vs real services?   | [when-to-mock.md           |

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
