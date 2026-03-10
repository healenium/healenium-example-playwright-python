"""
Locator API - iframe - Tests.
Supports XPath, CSS, id selectors within frame path: frame selector >> ... >> element selector.
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_iframe_change_frame_title_input_field_expect(page: Page):
    iframe = page.frame_locator('iframe[title="Iframe Example"]')
    input_field = iframe.locator("#iframe_input")
    expect(input_field).to_be_visible()
    iframe.locator("#iframe_Submit").click()
    healed = iframe.locator("#iframe_input")
    expect(healed).to_be_visible()


@pytest.mark.slow
def test_iframe_change_frame_title_select_option_action(page: Page):
    iframe = page.frame_locator('iframe[title="Iframe Example"]')
    select_el = iframe.locator("#iframe_select_item")
    select_el.select_option(label="iframe Item 1", timeout=TIMEOUT)
    expect(select_el).to_have_value("11")
    iframe.locator("#iframe_Submit").click()
    healed = iframe.locator("#iframe_select_item")
    healed.select_option(label="iframe Item 2", timeout=TIMEOUT)
    expect(healed).to_have_value("22")


@pytest.mark.slow
def test_iframe_change_all_nested_path(page: Page):
    input_field = (
        page.frame_locator('iframe[title="Iframe Example"]')
        .frame_locator('iframe[title="Nested iframe Example"]')
        .locator("#iframe_2_input")
    )
    expect(input_field).to_be_visible()
    page.frame_locator('iframe[title="Iframe Example"]').locator("#iframe_Submit").click(timeout=TIMEOUT)
    page.locator("#Submit").click(timeout=TIMEOUT)
    healed = (
        page.frame_locator('iframe[title="Iframe Example"]')
        .frame_locator('iframe[title="Nested iframe Example"]')
        .locator("#iframe_2_input")
    )
    expect(healed).to_be_visible()
