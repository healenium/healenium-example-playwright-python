"""
Locator API - Action Methods - Tests.
"""
import os
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"
TEST_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "test-data", "test-file.txt")


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_click_action(page: Page):
    input_field = page.locator(".test_class")
    input_field.click(timeout=TIMEOUT)
    
    page.locator("#Submit").click()

    healed = page.locator(".test_class")
    healed.click(timeout=TIMEOUT)


@pytest.mark.slow
def test_double_click_action(page: Page):
    input_field = page.locator("input#change_id")
    input_field.dblclick(timeout=TIMEOUT)

    page.locator("#Submit").click()

    healed = page.locator("input#change_id")
    healed.dblclick(timeout=TIMEOUT)


@pytest.mark.slow
def test_blur_action(page: Page):
    input_field = page.locator("input#change_id")
    input_field.blur(timeout=TIMEOUT)

    page.locator("#Submit").click()

    healed = page.locator("input#change_id")
    healed.blur(timeout=TIMEOUT)


@pytest.mark.slow
def test_fill_and_clear_actions(page: Page):
    input_field = page.locator(".test_class")
    input_field.fill("Hello World", timeout=TIMEOUT)
    expect(input_field).to_have_value("Hello World")
    input_field.clear(timeout=TIMEOUT)
    expect(input_field).to_have_value("")
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    healed.fill("Hello World", timeout=TIMEOUT)
    expect(healed).to_have_value("Hello World")
    healed.clear(timeout=TIMEOUT)
    expect(healed).to_have_value("")


@pytest.mark.slow
def test_type_action(page: Page):
    input_field = page.locator(".test_class")
    input_field.type("Typing text slowly", timeout=TIMEOUT)
    expect(input_field).to_have_value("Typing text slowly")

    page.locator("#Submit").click()

    healed = page.locator(".test_class")
    healed.type("Typing text slowly", timeout=TIMEOUT)
    expect(healed).to_have_value("Typing text slowlyTyping text slowly")


@pytest.mark.slow
def test_press_sequentially_action(page: Page):
    input_field = page.locator(".test_class")
    input_field.press_sequentially("Sequential typing", delay=100, timeout=TIMEOUT)
    expect(input_field).to_have_value("Sequential typing")

    page.locator("#Submit").click()

    healed = page.locator(".test_class")
    healed.press_sequentially("Sequential typing", delay=100, timeout=TIMEOUT)
    expect(healed).to_have_value("Sequential typingSequential typing")


@pytest.mark.slow
def test_press_action(page: Page):
    input_field = page.locator("input#change_id")
    input_field.fill("Test text", timeout=TIMEOUT)
    input_field.press("Enter", timeout=TIMEOUT)

    page.locator("#Submit").click()

    healed = page.locator("input#change_id")
    healed.fill("Test text", timeout=TIMEOUT)
    healed.press("Enter", timeout=TIMEOUT)


@pytest.mark.slow
def test_hover_action(page: Page):
    input_field = page.locator("input#change_id")
    input_field.hover(timeout=TIMEOUT)

    page.locator("#Submit").click()

    healed = page.locator("input#change_id")
    healed.hover(timeout=TIMEOUT)


@pytest.mark.slow
def test_focus_and_blur_actions(page: Page):
    input_field = page.locator(".test_class")
    input_field.focus(timeout=TIMEOUT)
    expect(input_field).to_be_focused()
    input_field.blur(timeout=TIMEOUT)
    expect(input_field).not_to_be_focused()

    page.locator("#Submit").click()

    healed = page.locator(".test_class")
    healed.focus(timeout=TIMEOUT)
    expect(healed).to_be_focused()
    healed.blur(timeout=TIMEOUT)
    expect(healed).not_to_be_focused()


@pytest.mark.slow
def test_scroll_into_view_if_needed_action(page: Page):
    input_field = page.locator(".test_class")
    input_field.scroll_into_view_if_needed(timeout=TIMEOUT)
    expect(input_field).to_be_visible()

    page.locator("#Submit").click()

    healed = page.locator(".test_class")
    healed.scroll_into_view_if_needed(timeout=TIMEOUT)
    expect(healed).to_be_visible()


@pytest.mark.slow
def test_select_text_action(page: Page):
    input_field = page.locator(".test_class")
    input_field.fill("Text to select", timeout=TIMEOUT)
    input_field.select_text(timeout=TIMEOUT)
    expect(input_field).to_be_focused()

    page.locator("#Submit").click()

    healed = page.locator(".test_class")
    healed.fill("Text to select", timeout=TIMEOUT)
    healed.select_text(timeout=TIMEOUT)
    expect(healed).to_be_focused()


@pytest.mark.slow
def test_select_option_action(page: Page):
    select_el = page.locator("#select_item")
    select_el.select_option(label="Item 1", timeout=TIMEOUT)

    page.locator("#Submit").click()

    healed = page.locator("#select_item")
    healed.select_option(label="Item 1", timeout=TIMEOUT)
    expect(healed).to_have_value("1")


@pytest.mark.slow
def test_set_input_files_action(page: Page):
    input_file = page.locator("#file_input")
    input_file.set_input_files(TEST_FILE, timeout=TIMEOUT)
    value = input_file.input_value(timeout=TIMEOUT)

    page.locator("#Submit").click()

    healed = page.locator("#file_input")
    healed.set_input_files(TEST_FILE, timeout=TIMEOUT)
    healed_value = healed.input_value(timeout=TIMEOUT)
    assert healed_value == value
