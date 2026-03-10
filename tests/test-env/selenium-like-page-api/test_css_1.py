"""
CSS 1 Locator Tests - Page API (query_selector).
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 9000
WAIT_TIMEOUT = 450


@pytest.mark.slow
def test_update_locator_for_element_with_css_attribute(page: Page):
    page.goto(
        "https://mdn.github.io/web-components-examples/life-cycle-callbacks/",
        wait_until="domcontentloaded",
    )
    add_square_btn = page.query_selector("//button[contains(@class, \"add\")]")
    assert add_square_btn is not None
    add_square_btn.click(timeout=TIMEOUT)
    square_element = page.query_selector('custom-square[color="red"]')
    assert square_element is not None
    assert square_element.is_visible()
    for _ in range(2):
        update_square_btn = page.query_selector("//button[contains(@class, \"update\")]")
        assert update_square_btn is not None
        update_square_btn.click(timeout=TIMEOUT)
        page.wait_for_timeout(WAIT_TIMEOUT)
        healed_square = page.query_selector('custom-square[color="red"]')
        assert healed_square is not None
        assert healed_square.is_visible()
