import re
from datetime import datetime, timedelta
import types
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock pyautogui for import
mock_pg = types.ModuleType('pyautogui')
mock_pg.FAILSAFE = False
mock_pg.alert = lambda *a, **k: None
mock_pg.confirm = lambda *a, **k: None
sys.modules['pyautogui'] = mock_pg

from modules.helpers import calculate_date_posted

def test_calculate_date_posted_extra_words():
    result = calculate_date_posted("Dallas, TX 3 days ago")
    assert result is not None
    delta = datetime.now() - result
    assert delta.days >= 3 and delta.days <= 4
