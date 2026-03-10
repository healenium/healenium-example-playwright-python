# Healenium Example - Playwright Python

Tests using [Playwright for Python](https://playwright.dev/python/) and pytest.

## Setup

**First time only** (create venv and install deps):

```bash
cd healenium-example-playwright-python
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

**Every new terminal** (only activate the venv):

```bash
cd healenium-example-playwright-python
source .venv/bin/activate
pytest -v
```

(Optional) Connect to Healenium proxy: set `PLAYWRIGHT_SERVER_URL` to your WebSocket endpoint (default: `ws://localhost:8095/hlm-playwright-proxy`).

## Running tests

- Run all tests (requires Healenium/remote browser or local Chromium):

  ```bash
  pytest
  ```

- Run with verbose output:

  ```bash
  pytest -v
  ```

- Run only tests that are not marked `slow`:

  ```bash
  pytest -m "not slow"
  ```

- Run a specific test file:

  ```bash
  pytest tests/test-env/playwright-specific/test_get_by.py -v
  ```

## Project structure

- `conftest.py` – Pytest/Playwright config: `connect_options` (WebSocket to Healenium), timeouts.
- `tests/test-env/playwright-specific/` – Locator API tests (getBy, chain, iframe, actions, expect, etc.).
- `tests/test-env/selenium-like-locator-api/` – Locator-based tests (CSS, XPath, simple, general, parent-child).
- `tests/test-env/selenium-like-page-api/` – Page API tests using `query_selector` (ElementHandle-style).

Tests target the same Healenium test env URL as the Node.js example: `https://healenium.github.io/healenium-test-env/index.html`.
