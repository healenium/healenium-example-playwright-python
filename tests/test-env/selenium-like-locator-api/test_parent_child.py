"""
Parent-Child Locator API Tests.
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
WAIT_TIMEOUT = 250
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_select_and_verify_several_inputs_css_first_child(page: Page):
    first_child = page.locator("test_tag:first-child")
    expect(first_child).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator("test_tag:first-child")
    expect(healed).to_be_visible()

@pytest.mark.slow
def test_select_and_verify_several_inputs_css_last_child(page: Page):
    last_child = page.locator("child_tag:last-child")
    expect(last_child).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator("child_tag:last-child")
    expect(healed).to_be_visible()
