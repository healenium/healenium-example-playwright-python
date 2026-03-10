"""
CSS 2 Locator Tests.
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
def test_update_locator_for_element_with_css_id_special_character(page: Page):
    change_name_element = page.locator(r"input#change\:name")
    expect(change_name_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator(r"input#change\:name")
    expect(healed).to_be_visible()


@pytest.mark.slow
def test_update_locator_for_element_with_css_element(page: Page):
    test_tag_element = page.locator("test_tag")
    expect(test_tag_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator("test_tag")
    expect(healed).to_be_visible()


@pytest.mark.slow
def test_update_locator_for_element_with_css_disabled(page: Page):
    disabled_element = page.locator("input:disabled")
    expect(disabled_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator("input:disabled")
    expect(healed).to_be_visible()


@pytest.mark.slow
def test_update_locator_for_element_with_css_enabled(page: Page):
    enabled_element = page.locator("textarea:enabled")
    expect(enabled_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator("textarea:enabled")
    expect(healed).to_be_visible()


@pytest.mark.slow
def test_update_locator_for_element_with_css_class_name(page: Page):
    test_class_element = page.locator(".test_class")
    expect(test_class_element).to_be_visible()
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator(".test_class")
    expect(healed).to_be_visible()
