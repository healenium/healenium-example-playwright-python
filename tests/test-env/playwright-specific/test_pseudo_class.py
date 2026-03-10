"""
Locator API - pseudo-class selectors - Tests.
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 3000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_text_selector(page: Page):
    expect(page.locator("text=Green Item")).to_be_visible()
    page.locator("#Submit").click(timeout=TIMEOUT)
    expect(page.locator("text=Green Item")).to_be_visible()


@pytest.mark.slow
def test_data_testid_selector(page: Page):
    expect(page.locator("data-testid=change_testId")).to_be_visible()
    page.locator("#Submit").click(timeout=TIMEOUT)
    expect(page.locator("data-testid=change_testId")).to_be_visible()


@pytest.mark.slow
def test_xpath_selector(page: Page):
    expect(page.locator("xpath=//input[@id=\"change_id\"]")).to_be_visible()
    page.locator("#Submit").click(timeout=TIMEOUT)
    expect(page.locator("xpath=//input[@id=\"change_id\"]")).to_be_visible()


@pytest.mark.slow
def test_css_selector(page: Page):
    expect(page.locator("css=.test_class")).to_be_visible()
    page.locator("#Submit").click(timeout=TIMEOUT)
    expect(page.locator("css=.test_class")).to_be_visible()


@pytest.mark.slow
def test_id_selector(page: Page):
    expect(page.locator("id=change_id")).to_be_visible()
    page.locator("#Submit").click(timeout=TIMEOUT)
    expect(page.locator("id=change_id")).to_be_visible()
