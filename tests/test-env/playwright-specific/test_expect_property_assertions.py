"""
Expect - Property Assertions (healing).
"""
import re
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_to_have_attribute(page: Page):
    loc = page.locator("#change_id")
    expect(loc).to_have_attribute("type", "text", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#change_id")
    expect(healed).to_have_attribute("type", "text", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_js_property(page: Page):
    loc = page.locator("#change_id")
    expect(loc).to_have_js_property("type", "text", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#change_id")
    expect(healed).to_have_js_property("type", "text", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_class(page: Page):
    loc = page.locator("#change_id")
    expect(loc).to_have_class(re.compile(r"input1"), timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#change_id")
    expect(healed).to_have_class(re.compile(r"input1"), timeout=TIMEOUT)


@pytest.mark.slow
def test_to_contain_class(page: Page):
    loc = page.locator("#change_id")
    expect(loc).to_contain_class("input1", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#change_id")
    expect(healed).to_contain_class("input1", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_css(page: Page):
    loc = page.locator("#change_id")
    expect(loc).to_have_css("display", re.compile(r"block|inline-block|inline"), timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#change_id")
    expect(healed).to_have_css("display", re.compile(r"block|inline-block|inline"), timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_id(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_have_id("change_className", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_have_id("change_className", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_role(page: Page):
    loc = page.locator(".test_class")
    expect(loc).to_have_role("textbox", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_have_role("textbox", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_contain_text(page: Page):
    loc = page.locator("#select_item")
    expect(loc).to_contain_text("Select an item", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#select_item")
    expect(healed).to_contain_text("Select an item", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_text(page: Page):
    loc = page.locator("#drop1")
    expect(loc).to_have_text("Drop Zone", timeout=TIMEOUT)
    page.locator("#Submit_checkbox").click()
    healed = page.locator("#drop1")
    expect(healed).to_have_text("Drop Zone", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_text_multiline(page: Page):
    loc = page.locator("#select_item")
    expect(loc).to_have_text(
        re.compile(r"Select an item\s+Item 1\s+Item 2\s+Item 3\s+Item 4"),
        timeout=TIMEOUT,
    )
    page.locator("#Submit").click()
    healed = page.locator("#select_item")
    expect(healed).to_have_text(
        re.compile(r"Select an item\s+Item 1\s+Item 2\s+Item 3\s+Item 4"),
        timeout=TIMEOUT,
    )


@pytest.mark.slow
def test_to_have_value(page: Page):
    loc = page.locator(".test_class")
    loc.fill("hello", timeout=TIMEOUT)
    expect(loc).to_have_value("hello", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator(".test_class")
    expect(healed).to_have_value("hello", timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_values(page: Page):
    loc = page.locator("#select_item")
    loc.select_option(value=["1", "2"], timeout=TIMEOUT)
    expect(loc).to_have_values(["1", "2"], timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#select_item")
    expect(healed).to_have_values(["1", "2"], timeout=TIMEOUT)


@pytest.mark.slow
def test_to_have_count(page: Page):
    loc = page.get_by_text("Green Item")
    expect(loc).to_have_count(1)
    page.locator("#Submit").click()
    healed = page.get_by_text("Green Item")
    expect(healed).to_have_count(1)
