"""
CSS 1 Locator Tests (custom-square / MDN page).
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
WAIT_TIMEOUT = 250


@pytest.mark.slow
def test_update_locator_for_element_with_css_attribute(page: Page):
    page.goto(
        "https://mdn.github.io/web-components-examples/life-cycle-callbacks/",
        wait_until="load",
    )
    add_square_btn = page.locator("//button[contains(@class, \"add\")]")
    expect(add_square_btn).to_be_visible()
    add_square_btn.click(timeout=TIMEOUT)
    square_element = page.locator('custom-square[color="red"]')
    expect(square_element).to_be_visible()
    for i in range(2):
        update_square_btn = page.locator("//button[contains(@class, \"update\")]")
        expect(update_square_btn).to_be_visible()
        update_square_btn.click(timeout=TIMEOUT)
        page.wait_for_timeout(WAIT_TIMEOUT)
        healed_square = page.locator('custom-square[color="red"]')
        expect(healed_square).to_be_visible()
