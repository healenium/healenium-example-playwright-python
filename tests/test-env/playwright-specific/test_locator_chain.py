"""
Locator API - Chained Locators (healing) - Tests.
Playwright: use locators, chain to narrow down; each test: chain → action → click change → same chain (healing).
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_simple_chain_form_then_get_by_placeholder(page: Page):
    input_el = page.locator("#main_form").get_by_placeholder("Change: TestId")
    input_el.fill("chained", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.locator("#main_form").get_by_placeholder("Change: TestId")
    healed.fill("chained healed", timeout=TIMEOUT)
    expect(healed).to_have_value("chained healed")


@pytest.mark.slow
def test_simple_chain_form_then_get_by_role_textbox(page: Page):
    input_el = page.locator("#main_form").get_by_role("textbox", name="Field labeled by")
    input_el.fill("role and label", timeout=TIMEOUT)
    expect(input_el).to_have_value("role and label")
    page.locator("#Submit").click()
    healed = page.locator("#main_form").get_by_role("textbox", name="Field labeled by")
    healed.fill("role and label after heal", timeout=TIMEOUT)
    expect(healed).to_have_value("role and label after heal")


@pytest.mark.slow
def test_chain_with_and_get_by_placeholder_and_get_by_title(page: Page):
    input_el = (
        page.get_by_placeholder("Change: TestId")
        .and_(page.get_by_title("Validate change test id"))
    )
    input_el.fill("and chain", timeout=TIMEOUT)
    expect(input_el).to_have_value("and chain")
    page.locator("#Submit").click()
    healed = (
        page.get_by_placeholder("Change: TestId")
        .and_(page.get_by_title("Validate change test id"))
    )
    healed.fill("and chain healed", timeout=TIMEOUT)
    expect(healed).to_have_value("and chain healed")


@pytest.mark.slow
def test_chain_with_filter_drag_container_then_has_text(page: Page):
    green = page.locator(".drag-container").filter(has_text="Green Item")
    expect(green).to_be_visible(timeout=TIMEOUT)
    expect(green).to_have_count(1)
    page.locator("#Submit").click()
    healed = page.locator(".drag-container").filter(has_text="Green Item")
    expect(healed).to_be_visible(timeout=TIMEOUT)
    expect(healed).to_have_count(1)


@pytest.mark.slow
def test_chain_with_or_get_by_test_id_or_get_by_placeholder(page: Page):
    input_el = page.get_by_test_id("change_testId").or_(page.get_by_placeholder("Change: TestId"))
    input_el.fill("or chain", timeout=TIMEOUT)
    expect(input_el).to_have_value("or chain")
    page.locator("#Submit").click()
    healed = page.get_by_test_id("change_testId").or_(page.get_by_placeholder("Change: TestId"))
    healed.fill("or chain healed", timeout=TIMEOUT)
    expect(healed).to_have_value("or chain healed")


@pytest.mark.slow
def test_chain_with_or_get_by_title_or_get_by_test_id(page: Page):
    input_el = page.get_by_title("Validate change test id").or_(page.get_by_test_id("change_testId"))
    expect(input_el).to_be_visible(timeout=TIMEOUT)
    input_el.fill("or title testid", timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed = page.get_by_title("Validate change test id").or_(page.get_by_test_id("change_testId"))
    expect(healed).to_have_value("or title testid", timeout=TIMEOUT)
