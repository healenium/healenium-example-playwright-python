"""
Expect - Special Assertions (healing).
toMatchAriaSnapshot and other special assertions.
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_to_match_aria_snapshot(page: Page):
    snapshot = "- text: Drop Zone"
    loc = page.locator("#drop1")
    expect(loc).to_match_aria_snapshot(snapshot, timeout=TIMEOUT)
    page.locator("#Submit_checkbox").click()
    healed = page.locator("#drop1")
    expect(healed).to_match_aria_snapshot(snapshot, timeout=TIMEOUT)
