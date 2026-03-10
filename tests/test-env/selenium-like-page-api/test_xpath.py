"""
XPath Locator Tests - Page API (query_selector).
"""
import pytest
from playwright.sync_api import Page

TIMEOUT = 9000
WAIT_TIMEOUT = 450
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


def _accept_dialog(page: Page):
    page.on("dialog", lambda d: d.accept())


@pytest.mark.slow
def test_xpath_with_special_characters(page: Page):
    _accept_dialog(page)
    special = page.query_selector('//*[@id="change:name"]')
    assert special is not None
    special.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[@id="change:name"]')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_following(page: Page):
    _accept_dialog(page)
    following = page.query_selector('//*[@id="change_className"]/following::test_tag')
    assert following is not None
    following.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[@id="change_className"]/following::test_tag')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_contains(page: Page):
    _accept_dialog(page)
    contains = page.query_selector('//input[contains(@class, "test")]')
    assert contains is not None
    contains.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//input[contains(@class, "test")]')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_not_contains(page: Page):
    _accept_dialog(page)
    not_contains = page.query_selector(
        '//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    assert not_contains is not None
    not_contains.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector(
        '//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_following_sibling(page: Page):
    _accept_dialog(page)
    following_sibling = page.query_selector('//*[starts-with(@class, "test")]/following-sibling::*')
    assert following_sibling is not None
    following_sibling.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[starts-with(@class, "test")]/following-sibling::*')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_ancestor(page: Page):
    _accept_dialog(page)
    ancestor = page.query_selector(
        '(//*[starts-with(@class, "test")]/ancestor::div[@class="healenium-form validate-form"]//input)[1]'
    )
    assert ancestor is not None
    ancestor.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector(
        '(//*[starts-with(@class, "test")]/ancestor::div[@class="healenium-form validate-form"]//input)[1]'
    )
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_or(page: Page):
    _accept_dialog(page)
    or_el = page.query_selector('//*[@id="change_id" or @id="omg"]')
    assert or_el is not None
    or_el.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[@id="change_id" or @id="omg"]')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_and(page: Page):
    _accept_dialog(page)
    and_el = page.query_selector('//*[@id="change_id" and @type="text"]')
    assert and_el is not None
    and_el.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[@id="change_id" and @type="text"]')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_starts_with(page: Page):
    _accept_dialog(page)
    starts_with = page.query_selector('//*[starts-with(@class, "test")]')
    assert starts_with is not None
    starts_with.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[starts-with(@class, "test")]')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_preceding(page: Page):
    _accept_dialog(page)
    preceding = page.query_selector('//*[@id="change_className"]/preceding::*[@id="change_id"]')
    assert preceding is not None
    preceding.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[@id="change_className"]/preceding::*[@id="change_id"]')
    assert healed is not None
    healed.press("Enter")

@pytest.mark.slow
def test_xpath_descendant(page: Page):
    _accept_dialog(page)
    descendant = page.query_selector('//*[@id="descendant_change"]/descendant::input')
    assert descendant is not None
    descendant.press("Enter")
    submit_btn = page.query_selector("#Submit")
    assert submit_btn is not None
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.query_selector('//*[@id="descendant_change"]/descendant::input')
    assert healed is not None
    healed.press("Enter")
