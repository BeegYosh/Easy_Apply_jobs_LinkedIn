import os
import sys
import types
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Stub pyautogui to avoid import issues
mock_pg = types.ModuleType('pyautogui')
mock_pg.FAILSAFE = False
mock_pg.alert = lambda *a, **k: None
mock_pg.confirm = lambda *a, **k: None
sys.modules['pyautogui'] = mock_pg

from selenium.common.exceptions import ElementClickInterceptedException
from modules.clickers_and_finders import click_easy_apply_button


def test_click_easy_apply_button_intercepted(monkeypatch):
    driver = MagicMock()
    container = MagicMock()
    button = MagicMock()

    driver.find_element.return_value = container
    container.find_element.return_value = button
    button.click.side_effect = ElementClickInterceptedException()

    result = click_easy_apply_button(driver)

    driver.execute_script.assert_any_call("arguments[0].click()", button)
    assert result is True
