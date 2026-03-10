"""
Locator API - Information Methods - Tests.
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 3000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_text_content_method(page: Page):
    input_field = page.locator('#select_item option[value="1"]')
    text_content = input_field.text_content(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator('#select_item option[value="1"]')
    healed_text_content = healed.text_content(timeout=TIMEOUT)
    assert healed_text_content == text_content


@pytest.mark.slow
def test_inner_text_method(page: Page):
    element = page.locator('[name="dragRed"]')
    inner_text = element.inner_text(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator('[name="dragRed"]')
    healed_inner_text = healed.inner_text(timeout=TIMEOUT)
    assert healed_inner_text == inner_text


@pytest.mark.slow
def test_inner_html_method(page: Page):
    element = page.locator('[name="dragRed"]')
    inner_html = element.inner_html(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator('[name="dragRed"]')
    healed_inner_html = healed.inner_html(timeout=TIMEOUT)
    assert healed_inner_html == inner_html


@pytest.mark.slow
def test_input_value_method(page: Page):
    input_field = page.locator(".test_class")
    input_field.fill("Test value", timeout=TIMEOUT)
    input_value = input_field.input_value(timeout=TIMEOUT)
    assert input_value == "Test value"
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed.fill("Test value", timeout=TIMEOUT)
    healed_input_value = healed.input_value(timeout=TIMEOUT)
    assert healed_input_value == "Test value"


@pytest.mark.slow
def test_get_attribute_method(page: Page):
    input_field = page.locator(".test_class")
    attribute = input_field.get_attribute("name", timeout=TIMEOUT)
    assert attribute == "Field2"
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed_attribute = healed.get_attribute("name", timeout=TIMEOUT)
    assert healed_attribute == "Field2"


@pytest.mark.slow
def test_bounding_box_method(page: Page):
    input_field = page.locator("#select_item")
    bounding_box = input_field.bounding_box(timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#select_item")
    healed_bounding_box = healed.bounding_box(timeout=TIMEOUT)
    assert healed_bounding_box is not None and bounding_box is not None
    assert healed_bounding_box["width"] == bounding_box["width"]
    assert healed_bounding_box["height"] == bounding_box["height"]


@pytest.mark.slow
def test_is_enabled_method(page: Page):
    input_field = page.locator(".test_class")
    is_enabled = input_field.is_enabled(timeout=TIMEOUT)
    assert is_enabled is True
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed_is_enabled = healed.is_enabled(timeout=TIMEOUT)
    assert healed_is_enabled is True


@pytest.mark.slow
def test_is_disabled_method(page: Page):
    input_field = page.locator(".test_class")
    is_disabled = input_field.is_disabled(timeout=TIMEOUT)
    assert is_disabled is False
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed_is_disabled = healed.is_disabled(timeout=TIMEOUT)
    assert healed_is_disabled is False


@pytest.mark.slow
def test_is_editable_method(page: Page):
    input_field = page.locator(".test_class")
    is_editable = input_field.is_editable(timeout=TIMEOUT)
    assert is_editable is True
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed_is_editable = healed.is_editable(timeout=TIMEOUT)
    assert healed_is_editable is True
