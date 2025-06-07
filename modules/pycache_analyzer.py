import os
from typing import List

def find_pycache_dirs(base_path: str) -> List[str]:
    """Return a list of all __pycache__ directories under *base_path*."""
    pycache_dirs = []
    for root, dirs, _ in os.walk(base_path):
        for d in dirs:
            if d == "__pycache__":
                pycache_dirs.append(os.path.join(root, d))
    return pycache_dirs
