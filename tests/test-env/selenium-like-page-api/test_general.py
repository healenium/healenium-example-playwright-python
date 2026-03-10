"""
General Locator Tests - Page API (query_selector).
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
def test_button_click_with_find_by_annotation(page: Page):
    page.on("dialog", lambda d: d.accept())
    submit_alert_btn = page.query_selector("#submit_alert")
    assert submit_alert_btn is not None
    submit_alert_btn.click(timeout=TIMEOUT)
    change_id_element = page.query_selector("#change_id")
    assert change_id_element is not None
    change_id_element.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector("#change_id")
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_input_fields_click_with_find_by_annotation(page: Page):
    test_class_element = page.query_selector("input.test_class")
    assert test_class_element is not None
    test_class_element.press("Enter")
    test_tag_element = page.query_selector("test_tag#change_element")
    assert test_tag_element is not None
    class_attr = test_tag_element.get_attribute("class")
    assert class_attr == "shadow-input1"
    test_tag_element.is_visible()
    change_name_element = page.query_selector('input[name="change_name"]')
    assert change_name_element is not None
    change_name_element.press("Enter")
    link_element = page.query_selector('a:has-text("Change: LinkText, PartialLinkText")')
    assert link_element is not None
    link_element.is_visible()
    link_class_attr = link_element.get_attribute("class")
    assert link_class_attr == "input1"
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed_test_class = page.query_selector("input.test_class")
    assert healed_test_class is not None
    healed_test_class.press("Enter")
    healed_test_tag = page.query_selector("test_tag#change_element")
    assert healed_test_tag is not None
    healed_class_attr = healed_test_tag.get_attribute("class")
    assert healed_class_attr == class_attr
    healed_test_tag.is_visible()
    healed_change_name = page.query_selector('input[name="change_name"]')
    assert healed_change_name is not None
    healed_change_name.press("Enter")
    healed_link = page.query_selector('a:has-text("Change: LinkText, PartialLinkText")')
    assert healed_link is not None
    healed_link.is_visible()
    healed_link_class = healed_link.get_attribute("class")
    assert healed_link_class == link_class_attr

@pytest.mark.slow
def test_checkbox_verify_with_find_by_annotation(page: Page):
    checkbox1 = page.query_selector("input.input1#form_checked1")
    assert checkbox1 is not None
    checkbox2 = page.query_selector("input.input1#form_checked2")
    assert checkbox2 is not None
    checkbox3 = page.query_selector("input.input1#form_checked3")
    assert checkbox3 is not None
    submit_checkbox_btn = page.query_selector("#Submit_checkbox")
    assert submit_checkbox_btn is not None
    submit_checkbox_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed_cb1 = page.query_selector("input.input1#form_checked1")
    assert healed_cb1 is not None
    healed_cb2 = page.query_selector("input.input1#form_checked2")
    assert healed_cb2 is not None
    healed_cb3 = page.query_selector("input.input1#form_checked3")
    assert healed_cb3 is not None

@pytest.mark.slow
def test_input_field_enable_to_disable_with_find_by_annotation(page: Page):
    enabled_element = page.query_selector("#change_enabled")
    assert enabled_element is not None
    assert enabled_element.is_enabled() is True
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    disabled_element = page.query_selector("#change_enabled")
    assert disabled_element is not None
    assert disabled_element.is_disabled() is True

@pytest.mark.slow
def test_checkbox_checked_to_unchecked_with_find_by_annotation(page: Page):
    checked_element = page.query_selector("#change_checked")
    assert checked_element is not None
    assert checked_element.is_checked() is True
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    unchecked_element = page.query_selector("#change_checked")
    assert unchecked_element is not None
    assert unchecked_element.is_checked() is False
