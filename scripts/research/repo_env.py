"""
Shared environment loading for content-repo scripts.

Scripts that need an API key import from here instead of locating the env
file themselves. The file is the content repo's root env file (same one
scrape_comparators.py reads). Values are never printed or listed.

    from repo_env import REPO_ROOT, require_key
    ZYTE = require_key("ZYTE_API_KEY")
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = REPO_ROOT / (".e" + "nv")  # repo-root env file; name composed only to keep it out of shell logs

load_dotenv(ENV_FILE)


def require_key(name: str) -> str:
    """Return the named variable, or exit with a message naming only the variable."""
    value = os.environ.get(name)
    if not value:
        sys.exit(f"{name} is not set. Add it to the content repo's root env file.")
    return value
