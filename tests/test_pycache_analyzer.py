import os
import sys
import types

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import pycache_analyzer


def test_find_pycache_dirs(tmp_path):
    # create sample directory structure with __pycache__ dirs
    (tmp_path / 'a' / '__pycache__').mkdir(parents=True)
    (tmp_path / 'b' / 'c' / '__pycache__').mkdir(parents=True)
    results = pycache_analyzer.find_pycache_dirs(str(tmp_path))
    expected = {
        os.path.join(tmp_path, 'a', '__pycache__'),
        os.path.join(tmp_path, 'b', 'c', '__pycache__'),
    }
    assert set(results) == expected


def test_find_pycache_dirs_empty(tmp_path):
    # no __pycache__ directories
    (tmp_path / 'a').mkdir()
    results = pycache_analyzer.find_pycache_dirs(str(tmp_path))
    assert results == []
