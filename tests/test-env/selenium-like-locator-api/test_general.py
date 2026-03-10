"""
General Locator API Tests.
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 3000
WAIT_TIMEOUT = 250
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_button_click_with_find_by_annotation(page: Page):
    page.on("dialog", lambda d: d.accept())
    submit_alert_btn = page.locator("#submit_alert")
    expect(submit_alert_btn).to_be_visible()
    submit_alert_btn.click(timeout=TIMEOUT)
    change_id_element = page.locator("#change_id")
    change_id_element.press("Enter", timeout=TIMEOUT)
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed_change_id = page.locator("#change_id")
    healed_change_id.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_input_fields_click_with_find_by_annotation(page: Page):
    test_class_element = page.locator("input.test_class")
    expect(test_class_element).to_be_visible()
    test_class_element.press("Enter")
    test_tag_element = page.locator("test_tag#change_element")
    expect(test_tag_element).to_be_visible()
    test_tag_element.is_visible()
    class_attr = test_tag_element.get_attribute("class")
    assert class_attr == "shadow-input1"
    change_name_element = page.locator('input[name="change_name"]')
    expect(change_name_element).to_be_visible()
    link_element = page.locator('a:has-text("Change: LinkText, PartialLinkText")')
    expect(link_element).to_be_visible()
    link_element.is_visible()
    link_class_attr = link_element.get_attribute("class")
    assert link_class_attr == "input1"
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed_test_class = page.locator("input.test_class")
    expect(healed_test_class).to_be_visible()
    healed_test_class.press("Enter", timeout=TIMEOUT)
    healed_test_tag = page.locator("test_tag#change_element")
    expect(healed_test_tag).to_be_visible()
    healed_test_tag.is_visible(timeout=TIMEOUT)
    healed_class_attr = healed_test_tag.get_attribute("class", timeout=TIMEOUT)
    assert healed_class_attr == class_attr
    healed_change_name = page.locator('input[name="change_name"]')
    expect(healed_change_name).to_be_visible()
    healed_change_name.press("Enter", timeout=TIMEOUT)
    healed_link = page.locator('a:has-text("Change: LinkText, PartialLinkText")')
    expect(healed_link).to_be_visible()
    healed_link.is_visible()
    healed_link_class = healed_link.get_attribute("class", timeout=TIMEOUT)
    assert healed_link_class == link_class_attr

@pytest.mark.slow
def test_checkbox_verify_with_find_by_annotation(page: Page):
    checkbox1 = page.locator("input.input1#form_checked1")
    expect(checkbox1).to_be_visible()
    checkbox2 = page.locator("input.input1#form_checked2")
    expect(checkbox2).to_be_visible()
    checkbox3 = page.locator("input.input1#form_checked3")
    expect(checkbox3).to_be_visible()
    submit_checkbox_btn = page.locator("#Submit_checkbox")
    expect(submit_checkbox_btn).to_be_visible()
    submit_checkbox_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed_cb1 = page.locator("input.input1#form_checked1")
    expect(healed_cb1).to_be_visible()
    healed_cb2 = page.locator("input.input1#form_checked2")
    expect(healed_cb2).to_be_visible()
    healed_cb3 = page.locator("input.input1#form_checked3")
    expect(healed_cb3).to_be_visible()

@pytest.mark.slow
def test_input_field_enable_to_disable_with_find_by_annotation(page: Page):
    enabled_element = page.locator("#change_enabled")
    expect(enabled_element).to_be_visible()
    assert enabled_element.is_enabled() is True
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    disabled_element = page.locator("#change_enabled")
    expect(disabled_element).to_be_visible()
    assert disabled_element.is_disabled() is True

@pytest.mark.slow
def test_checkbox_checked_to_unchecked_with_find_by_annotation(page: Page):
    checked_element = page.locator("#change_checked")
    expect(checked_element).to_be_visible()
    assert checked_element.is_checked() is True
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    unchecked_element = page.locator("#change_checked")
    expect(unchecked_element).to_be_visible()
    assert unchecked_element.is_checked() is False
