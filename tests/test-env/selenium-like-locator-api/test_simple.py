"""
Simple Locator API Tests (locator-based, no page.$).
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
def test_update_locator_for_element_with_css_id(page: Page):
    id_element = page.locator("#change_id")
    expect(id_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    change_id_element = page.locator("#change_id")
    expect(change_id_element).to_be_visible()


@pytest.mark.slow
def test_update_locator_for_element_with_css_enabled(page: Page):
    enabled_element = page.locator("textarea:enabled")
    expect(enabled_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    changed_enabled_element = page.locator("textarea:enabled")
    expect(changed_enabled_element).to_be_visible()


@pytest.mark.slow
def test_xpath_not_contains(page: Page):
    not_contains_element = page.locator(
        'xpath=//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    expect(not_contains_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    changed_not_contains = page.locator(
        'xpath=//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    expect(changed_not_contains).to_be_visible()
