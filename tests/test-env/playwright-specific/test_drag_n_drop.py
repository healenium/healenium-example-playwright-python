"""
Locator API - Drag and Drop - Tests.
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 5000
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


@pytest.mark.slow
def test_source_playwright_specific(page: Page):
    draggable = page.locator(".drag-container").get_by_text("Green Item")
    droppable = page.locator("#drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed_draggable = page.locator(".drag-container").get_by_text("Green Item")
    healed_droppable = page.locator("#drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_source_xpath(page: Page):
    draggable = page.locator('//div[@class="drag-container"]/div[@name="dragRed"]')
    droppable = page.locator("#drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit").click()
    healed_draggable = page.locator('//div[@class="drag-container"]/div[@name="dragRed"]')
    healed_droppable = page.locator("#drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_target_playwright_specific(page: Page):
    draggable = page.locator(".drag-container").get_by_text("Green Item")
    droppable = page.get_by_test_id("testid_drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit_checkbox").click()
    healed_draggable = page.locator(".drag-container").get_by_text("Green Item")
    healed_droppable = page.get_by_test_id("testid_drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_target_css(page: Page):
    draggable = page.locator(".drag-container").get_by_text("Green Item")
    droppable = page.locator("#drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit_checkbox").click()
    healed_draggable = page.locator(".drag-container").get_by_text("Green Item")
    healed_droppable = page.locator("#drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_source_and_target_playwright_specific_both(page: Page):
    draggable = page.locator(".drag-container").get_by_text("Green Item")
    droppable = page.get_by_test_id("testid_drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit").click()
    page.locator("#Submit_checkbox").click()
    healed_draggable = page.locator(".drag-container").get_by_text("Green Item")
    healed_droppable = page.get_by_test_id("testid_drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_source_and_target_xpath_css(page: Page):
    draggable = page.locator('//div[@class="drag-container"]/div[@name="dragRed"]')
    droppable = page.locator("#drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit").click()
    page.locator("#Submit_checkbox").click()
    healed_draggable = page.locator('//div[@class="drag-container"]/div[@name="dragRed"]')
    healed_droppable = page.locator("#drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_source_and_target_xpath_playwright_specific(page: Page):
    draggable = page.locator('//div[@class="drag-container"]/div[@name="dragRed"]')
    droppable = page.get_by_test_id("testid_drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit").click()
    page.locator("#Submit_checkbox").click()
    healed_draggable = page.locator('//div[@class="drag-container"]/div[@name="dragRed"]')
    healed_droppable = page.get_by_test_id("testid_drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_source_and_target_playwright_specific_css(page: Page):
    draggable = page.locator(".drag-container").get_by_text("Green Item")
    droppable = page.locator("#drop1")
    draggable.drag_to(droppable, timeout=TIMEOUT)
    page.locator("#Submit").click()
    page.locator("#Submit_checkbox").click()
    healed_draggable = page.locator(".drag-container").get_by_text("Green Item")
    healed_droppable = page.locator("#drop1")
    healed_draggable.drag_to(healed_droppable, timeout=TIMEOUT)


@pytest.mark.slow
def test_page_drag_and_drop(page: Page):
    page.drag_and_drop(
        '//div[@class="drag-container"]/div[@name="dragRed"]',
        "#drop1",
        timeout=TIMEOUT,
    )
    page.locator("#Submit").click()
    page.locator("#Submit_checkbox").click()
    page.drag_and_drop(
        '//div[@class="drag-container"]/div[@name="dragRed"]',
        "#drop1",
        timeout=TIMEOUT,
    )
