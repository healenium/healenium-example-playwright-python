"""
Locator API - getBy - Tests (Python port from healenium-example-playwright-nodejs).
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_get_by_role_img_alt(page: Page):
    expect(page.locator("img#logo_img")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("img#logo_img")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_role_textbox_aria_label(page: Page):
    expect(page.locator("input#change_below_element")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("input#change_below_element")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_role_textbox_aria_labelledby(page: Page):
    expect(page.locator("input#change_className")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("input#change_className")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_text(page: Page):
    expect(page.locator("div.draggable-item.green-item")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("div.draggable-item.green-item")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_label(page: Page):
    expect(page.locator("input#newValue")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("input#newValue")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_placeholder(page: Page):
    expect(page.locator("input#validate_testId")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("input#validate_testId")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_alt_text(page: Page):
    expect(page.locator("img#logo_img")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("img#logo_img")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_title(page: Page):
    expect(page.locator("input#validate_testId")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("input#validate_testId")).to_be_visible(timeout=TIMEOUT)


@pytest.mark.slow
def test_get_by_test_id(page: Page):
    expect(page.locator("input#validate_testId")).to_be_visible(timeout=TIMEOUT)
    page.locator("#Submit").click()
    expect(page.locator("input#validate_testId")).to_be_visible(timeout=TIMEOUT)
