"""
Locator API - Utility Methods - Tests.
"""
import json
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_describe_action(page: Page):
    change_id_input = page.locator("input#change_id")
    change_class_input = page.locator(".test_class")
    change_id_input.click(timeout=TIMEOUT)
    change_class_input.fill("Test description", timeout=TIMEOUT)
    expect(change_id_input).to_be_visible()
    expect(change_class_input).to_have_value("Test description")
    page.locator("#Submit").click()
    healed_change_id = page.locator("input#change_id")
    healed_change_class = page.locator(".test_class")
    healed_change_id.click(timeout=TIMEOUT)
    healed_change_class.fill("Test description", timeout=TIMEOUT)
    expect(healed_change_id).to_be_visible()
    expect(healed_change_class).to_have_value("Test description")


@pytest.mark.slow
def test_aria_snapshot_action(page: Page):
    change_id_input = page.locator("input#change_id")
    input_aria_snapshot = change_id_input.aria_snapshot(timeout=TIMEOUT)
    stringified = json.dumps(input_aria_snapshot, indent=2)
    assert input_aria_snapshot is not None
    assert "textbox" in stringified
    page.locator("#Submit").click()
    healed = page.locator("input#change_id")
    healed_snapshot = healed.aria_snapshot(timeout=TIMEOUT)
    healed_stringified = json.dumps(healed_snapshot, indent=2)
    assert healed_snapshot is not None
    assert "textbox" in healed_stringified


@pytest.mark.slow
def test_dispatch_event_action(page: Page):
    input_field = page.locator(".test_class")
    child_tag = page.locator("child_tag#change_element_last_child")
    test_tag = page.locator("test_tag#change_element")
    change_name_input = page.locator('input[name="change_name"]')
    input_field.dispatch_event("keydown", {"key": "A"}, timeout=TIMEOUT)
    child_tag.dispatch_event("customEvent", {"detail": "custom data"}, timeout=TIMEOUT)
    test_tag.dispatch_event("click", timeout=TIMEOUT)
    change_name_input.dispatch_event("input", {"data": "test"}, timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed_input = page.locator(".test_class")
    healed_child = page.locator("child_tag#change_element_last_child")
    healed_test = page.locator("test_tag#change_element")
    healed_name = page.locator('input[name="change_name"]')
    healed_input.dispatch_event("keydown", {"key": "A"}, timeout=TIMEOUT)
    healed_child.dispatch_event("customEvent", {"detail": "custom data"}, timeout=TIMEOUT)
    healed_test.dispatch_event("click", timeout=TIMEOUT)
    healed_name.dispatch_event("input", {"data": "test"}, timeout=TIMEOUT)


@pytest.mark.slow
def test_wait_for_action(page: Page):
    test_class_input = page.locator(".test_class")
    test_class_input.wait_for(state="visible", timeout=TIMEOUT)
    test_class_input.fill("WaitFor test", timeout=TIMEOUT)
    expect(test_class_input).to_have_value("WaitFor test", timeout=TIMEOUT)
    test_class_input.wait_for(state="attached", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed.wait_for(state="visible", timeout=TIMEOUT)
    healed.fill("WaitFor test", timeout=TIMEOUT)
    expect(healed).to_have_value("WaitFor test", timeout=TIMEOUT)
    healed.wait_for(state="attached", timeout=TIMEOUT)

