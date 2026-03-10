"""
Locator API - Checkbox Information Methods - Tests.
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 3000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_is_checked(page: Page):
    checkbox = page.locator("input.input1#form_checked1")
    checkbox.check(timeout=TIMEOUT)
    is_checked = checkbox.is_checked(timeout=TIMEOUT)
    assert is_checked is True
    page.locator("#Submit_checkbox").click()
    healed = page.locator("input.input1#form_checked1")
    healed.check(timeout=TIMEOUT)
    healed_is_checked = healed.is_checked(timeout=TIMEOUT)
    assert healed_is_checked is True
