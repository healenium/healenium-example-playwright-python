"""
Parent-Child Locator Tests - Page API (query_selector).
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 9000
WAIT_TIMEOUT = 450
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_select_and_verify_several_inputs_css_first_child(page: Page):
    first_child = page.query_selector("test_tag:first-child")
    assert first_child is not None
    assert first_child.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector("test_tag:first-child")
    assert healed is not None
    assert healed.is_visible()

@pytest.mark.slow
def test_select_and_verify_several_inputs_css_last_child(page: Page):
    last_child = page.query_selector("child_tag:last-child")
    assert last_child is not None
    assert last_child.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector("child_tag:last-child")
    assert healed is not None
    assert healed.is_visible()
