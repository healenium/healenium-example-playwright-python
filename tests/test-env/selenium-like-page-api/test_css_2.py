"""
CSS 2 Locator Tests - Page API (query_selector).
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
def test_update_locator_for_element_with_css_id_special_character(page: Page):
    change_name = page.query_selector(r"input#change\:name")
    assert change_name is not None
    assert change_name.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector(r"input#change\:name")
    assert healed is not None
    assert healed.is_visible()

@pytest.mark.slow
def test_update_locator_for_element_with_css_element(page: Page):
    test_tag = page.query_selector("test_tag")
    assert test_tag is not None
    assert test_tag.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector("test_tag")
    assert healed is not None
    assert healed.is_visible()

@pytest.mark.slow
def test_update_locator_for_element_with_css_disabled(page: Page):
    disabled = page.query_selector("input:disabled")
    assert disabled is not None
    assert disabled.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector("input:disabled")
    assert healed is not None
    assert healed.is_visible()

@pytest.mark.slow
def test_update_locator_for_element_with_css_enabled(page: Page):
    enabled = page.query_selector("textarea:enabled")
    assert enabled is not None
    assert enabled.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector("textarea:enabled")
    assert healed is not None
    assert healed.is_visible()

@pytest.mark.slow
def test_update_locator_for_element_with_css_class_name(page: Page):
    test_class = page.query_selector(".test_class")
    assert test_class is not None
    assert test_class.is_visible()
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector(".test_class")
    assert healed is not None
    assert healed.is_visible()
