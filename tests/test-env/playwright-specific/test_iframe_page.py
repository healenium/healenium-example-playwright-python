"""
iframe tests using Page API (query_selector / content_frame) - Selenium-like.
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 5000
WAIT_TIMEOUT = 250
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


def _wait(page: Page, ms: int = WAIT_TIMEOUT):
    page.wait_for_timeout(ms)


@pytest.mark.slow
def test_iframe_change_frame_title_healing(page: Page):
    iframe_el = page.query_selector('iframe[title="Iframe Example"]')
    assert iframe_el is not None
    frame = iframe_el.content_frame()
    assert frame is not None
    input_field = frame.query_selector("#iframe_input")
    assert input_field is not None
    input_field.click(timeout=TIMEOUT)
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    _wait(page)
    healed_iframe_el = page.query_selector('iframe[title="Iframe Example"]')
    _wait(page)
    assert healed_iframe_el is not None
    healed_frame = healed_iframe_el.content_frame()
    healed_input = healed_frame.query_selector("#iframe_input") if healed_frame else None
    _wait(page)
    assert healed_input is not None
    healed_input.click(timeout=TIMEOUT)


@pytest.mark.slow
def test_iframe_change_input_field_healing(page: Page):
    iframe_el = page.query_selector('iframe[title="Iframe Example"]')
    assert iframe_el is not None
    frame = iframe_el.content_frame()
    assert frame is not None
    input_field = frame.query_selector("#iframe_input")
    assert input_field is not None
    input_field.click(timeout=TIMEOUT)
    iframe_submit = frame.query_selector("#iframe_Submit")
    assert iframe_submit is not None
    iframe_submit.click(timeout=TIMEOUT)
    _wait(page)
    healed_input = frame.query_selector("#iframe_input")
    _wait(page)
    assert healed_input is not None
    healed_input.click(timeout=TIMEOUT)


@pytest.mark.slow
def test_iframe_change_frame_title_and_input_field_healing(page: Page):
    iframe_el = page.query_selector('iframe[title="Iframe Example"]')
    assert iframe_el is not None
    frame = iframe_el.content_frame()
    assert frame is not None
    input_field = frame.query_selector("#iframe_input")
    assert input_field is not None
    input_field.click(timeout=TIMEOUT)
    iframe_submit = frame.query_selector("#iframe_Submit")
    assert iframe_submit is not None
    iframe_submit.click(timeout=TIMEOUT)
    _wait(page)
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    _wait(page)
    healed_iframe_el = page.query_selector('iframe[title="Iframe Example"]')
    _wait(page)
    assert healed_iframe_el is not None
    healed_frame = healed_iframe_el.content_frame()
    healed_input = healed_frame.query_selector("#iframe_input") if healed_frame else None
    _wait(page)
    assert healed_input is not None
    healed_input.click(timeout=TIMEOUT)


@pytest.mark.slow
def test_iframe_change_nested_frame_healing(page: Page):
    iframe_el = page.query_selector('iframe[title="Iframe Example"]')
    assert iframe_el is not None
    frame = iframe_el.content_frame()
    assert frame is not None
    nested_el = frame.query_selector('iframe[title="Nested iframe Example"]')
    assert nested_el is not None
    nested_frame = nested_el.content_frame()
    assert nested_frame is not None
    input_field = nested_frame.query_selector("#iframe_2_input")
    assert input_field is not None
    input_field.click(timeout=TIMEOUT)
    iframe_submit = frame.query_selector("#iframe_Submit")
    assert iframe_submit is not None
    iframe_submit.click(timeout=TIMEOUT)
    _wait(page)
    healed_nested_el = frame.query_selector('iframe[title="Nested iframe Example"]')
    _wait(page)
    assert healed_nested_el is not None
    healed_nested_frame = healed_nested_el.content_frame()
    healed_input = healed_nested_frame.query_selector("#iframe_2_input") if healed_nested_frame else None
    _wait(page)
    assert healed_input is not None
    healed_input.click(timeout=TIMEOUT)
