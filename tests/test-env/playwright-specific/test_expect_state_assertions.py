"""
Expect - State Assertions (healing).
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_to_be_attached(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_be_attached(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_be_attached(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_visible(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_hidden(page: Page):
    loc = page.locator(".test_class")
    expect(loc).not_to_be_hidden(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).not_to_be_hidden(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_checked(page: Page):
    checkbox = page.locator("input.input1#form_checked1")
    expect(checkbox).to_be_checked(timeout=TIMEOUT)
    page.locator("#Submit_checkbox").click()
    healed = page.locator("input.input1#form_checked1")
    expect(healed).to_be_checked(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_disabled(page: Page):
    loc = page.locator(".test_class")
    expect(loc).not_to_be_disabled(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).not_to_be_disabled(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_enabled(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_be_enabled(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_be_enabled(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_editable(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_be_editable(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_be_editable(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_empty(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_be_empty(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_be_empty(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_focused(page: Page):
    loc = page.locator(".test_class")
    loc.focus(timeout=TIMEOUT)
    expect(loc).to_be_focused(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed.focus(timeout=TIMEOUT)
    expect(healed).to_be_focused(timeout=TIMEOUT)


@pytest.mark.slow
def test_to_be_in_viewport(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_be_in_viewport(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed.focus(timeout=TIMEOUT)
    expect(healed).to_be_in_viewport(timeout=TIMEOUT)
