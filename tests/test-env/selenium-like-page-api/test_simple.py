"""
Simple Locator Tests using Page API (query_selector / ElementHandle).
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
def test_update_locator_for_element_with_css_id(page: Page):
    id_element = page.query_selector("#change_id")
    assert id_element is not None
    assert id_element.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    change_id_element = page.query_selector("#change_id")
    assert change_id_element is not None
    assert change_id_element.is_visible()


@pytest.mark.slow
def test_update_locator_for_element_with_css_enabled(page: Page):
    enabled_element = page.query_selector("textarea:enabled")
    assert enabled_element is not None
    assert enabled_element.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    changed_enabled = page.query_selector("textarea:enabled")
    assert changed_enabled is not None
    assert changed_enabled.is_visible()


@pytest.mark.slow
def test_xpath_not_contains(page: Page):
    not_contains = page.query_selector(
        'xpath=//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    assert not_contains is not None
    assert not_contains.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    changed_not_contains = page.query_selector(
        'xpath=//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    assert changed_not_contains is not None
    assert changed_not_contains.is_visible()
