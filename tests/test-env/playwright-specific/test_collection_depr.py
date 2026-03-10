"""
Deprecated ElementHandle Methods - Tests.
element_handle() / locator.element_handle() equivalent: use locator then element_handle in Python.
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_element_handle_method_get_single_element_handle(page: Page):
    input_handle = page.locator(".test_class").element_handle(timeout=TIMEOUT)
    assert input_handle is not None
    input_handle.fill("New text value")
    assert input_handle.input_value() == "New text value"
    page.locator("#Submit").click()
    healed_handle = page.locator(".test_class").element_handle(timeout=TIMEOUT)
    assert healed_handle is not None
    assert healed_handle.input_value() == "New text value"
