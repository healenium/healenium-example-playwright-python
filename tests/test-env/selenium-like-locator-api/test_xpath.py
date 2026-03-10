"""
XPath Locator API Tests.
"""
import pytest
from playwright.sync_api import Page, expect

TIMEOUT = 5000
WAIT_TIMEOUT = 250
BASE_URL = "https://healenium.github.io/healenium-test-env/index.html"


@pytest.fixture(autouse=True)
def goto_test_env(page: Page):
    page.goto(BASE_URL, wait_until="load")


def _accept_dialog(page: Page):
    page.on("dialog", lambda dialog: dialog.accept())


@pytest.mark.slow
def test_xpath_with_special_characters(page: Page):
    _accept_dialog(page)
    special_char = page.locator('xpath=//*[@id="change:name"]')
    expect(special_char).to_be_visible()
    special_char.press("Enter")
    submit_btn = page.locator("#Submit")
    expect(submit_btn).to_be_visible()
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//*[@id="change:name"]')
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_following(page: Page):
    _accept_dialog(page)
    following = page.locator('xpath=//*[@id="change_className"]/following::test_tag')
    expect(following).to_be_visible()
    following.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//*[@id="change_className"]/following::test_tag')
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_not_contains(page: Page):
    _accept_dialog(page)
    not_contains = page.locator(
        'xpath=//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    expect(not_contains).to_be_visible()
    not_contains.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator(
        'xpath=//input[not(contains(@class, "input1")) and contains(@class, "test_class")]'
    )
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_following_sibling(page: Page):
    _accept_dialog(page)
    following_sibling = page.locator('xpath=//input[@class="test_class"]/following-sibling::*')
    expect(following_sibling).to_have_class("shadow-input1")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//input[@class="test_class"]/following-sibling::*')
    expect(healed).to_have_class("shadow-input1")

@pytest.mark.slow
def test_xpath_ancestor(page: Page):
    _accept_dialog(page)
    ancestor = page.locator(
        'xpath=(//*[starts-with(@class, "test")]/ancestor::div[@class="healenium-form validate-form"]//input)[1]'
    )
    expect(ancestor).to_be_visible()
    ancestor.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator(
        'xpath=(//*[starts-with(@class, "test")]/ancestor::div[@class="healenium-form validate-form"]//input)[1]'
    )
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_or(page: Page):
    _accept_dialog(page)
    or_el = page.locator('xpath=//*[@id="change_id" or @id="omg"]')
    expect(or_el).to_be_visible()
    or_el.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//*[@id="change_id" or @id="omg"]')
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_and(page: Page):
    _accept_dialog(page)
    and_el = page.locator('xpath=//*[@id="change_id" and @type="text"]')
    expect(and_el).to_be_visible()
    and_el.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//*[@id="change_id" and @type="text"]')
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_starts_with(page: Page):
    _accept_dialog(page)
    starts_with = page.locator('xpath=//*[starts-with(@class, "test") and @name="Field2"]')
    expect(starts_with).to_be_visible()
    starts_with.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//*[starts-with(@class, "test") and @name="Field2"]')
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_preceding(page: Page):
    _accept_dialog(page)
    preceding = page.locator('xpath=//*[@id="change_className"]/preceding::*[@id="change_id"]')
    expect(preceding).to_be_visible()
    preceding.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//*[@id="change_className"]/preceding::*[@id="change_id"]')
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)

@pytest.mark.slow
def test_xpath_descendant(page: Page):
    _accept_dialog(page)
    descendant = page.locator('xpath=//*[@id="descendant_change"]/descendant::input')
    expect(descendant).to_be_visible()
    descendant.press("Enter")
    submit_btn = page.locator("#Submit")
    submit_btn.click(timeout=TIMEOUT)
    page.wait_for_timeout(WAIT_TIMEOUT)
    healed = page.locator('xpath=//*[@id="descendant_change"]/descendant::input')
    expect(healed).to_be_visible()
    healed.press("Enter", timeout=TIMEOUT)
