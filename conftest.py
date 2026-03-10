"""
Pytest configuration for Healenium Playwright Python tests.
Connects to Healenium proxy (or local Playwright server) via WebSocket.
"""
import os
import pytest


@pytest.fixture(scope="session")
def connect_options():
    """Options for browser_type.connect() — WebSocket URL and timeout."""
    ws_url = os.environ.get(
        "PLAYWRIGHT_SERVER_URL",
        "ws://localhost:8095/hlm-playwright-proxy",
    )
    return {
        "ws_endpoint": ws_url,
        "timeout": 60000,
    }


@pytest.fixture(scope="session")
def browser(playwright, browser_type, connect_options):
    """Override plugin browser: connect to existing browser via WebSocket instead of launch.
    Ensures tests run through Healenium proxy (or PLAYWRIGHT_SERVER_URL).
    """
    browser_instance = browser_type.connect(**connect_options)
    yield browser_instance
    browser_instance.close()


@pytest.fixture(scope="session")
def browser_context_args():
    return {}


@pytest.fixture
def context(browser, browser_context_args):
    ctx = browser.new_context(**browser_context_args)
    ctx.set_default_timeout(120000)  # 2 min for actions
    ctx.set_default_navigation_timeout(120000)  # 2 min for navigation
    yield ctx
    ctx.close()
