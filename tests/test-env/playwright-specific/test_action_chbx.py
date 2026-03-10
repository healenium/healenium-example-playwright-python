"""
Locator API - CheckBox Action Methods - Tests.
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_check_action(page: Page):
    checkbox = page.locator("input.input1#form_checked1")
    checkbox.check(timeout=TIMEOUT)
    expect(checkbox).to_be_checked(timeout=TIMEOUT)

    page.locator("#Submit_checkbox").click()

    healed = page.locator("input.input1#form_checked1")
    healed.check(timeout=TIMEOUT)
    expect(healed).to_be_checked(timeout=TIMEOUT)


@pytest.mark.slow
def test_uncheck_action(page: Page):
    checkbox2 = page.locator("input.input1#form_checked2")
    checkbox2.uncheck(timeout=TIMEOUT)
    expect(checkbox2).not_to_be_checked(timeout=TIMEOUT)

    page.locator("#Submit_checkbox").click()

    healed = page.locator("input.input1#form_checked2")
    healed.uncheck(timeout=TIMEOUT)
    expect(healed).not_to_be_checked(timeout=TIMEOUT)


@pytest.mark.slow
def test_set_checked_true_action(page: Page):
    checkbox = page.locator("input.input1#form_checked1")
    checkbox.set_checked(True, timeout=TIMEOUT)
    expect(checkbox).to_be_checked(timeout=TIMEOUT)

    page.locator("#Submit_checkbox").click()

    healed = page.locator("input.input1#form_checked1")
    healed.set_checked(True, timeout=TIMEOUT)
    expect(healed).to_be_checked(timeout=TIMEOUT)


@pytest.mark.slow
def test_set_checked_false_action(page: Page):
    checkbox2 = page.locator("input.input1#form_checked2")
    checkbox2.set_checked(False, timeout=TIMEOUT)
    expect(checkbox2).not_to_be_checked(timeout=TIMEOUT)

    page.locator("#Submit_checkbox").click()

    healed = page.locator("input.input1#form_checked2")
    healed.set_checked(False, timeout=TIMEOUT)
    expect(healed).not_to_be_checked(timeout=TIMEOUT)


@pytest.mark.slow
def test_set_checked_with_force_action(page: Page):
    checkbox = page.locator("input.input1#form_checked1")
    checkbox.set_checked(True, force=True, timeout=TIMEOUT)
    expect(checkbox).to_be_checked(timeout=TIMEOUT)

    page.locator("#Submit_checkbox").click()

    healed = page.locator("input.input1#form_checked1")
    healed.set_checked(True, force=True, timeout=TIMEOUT)
    expect(healed).to_be_checked(timeout=TIMEOUT)

