
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
import time, os, platform
from pyrogram.errors import AccessTokenExpired, AccessTokenInvalid
from bot import botStartTime


def hrb(value, digits= 2, delim= "", postfix=""):
    """Return a human-readable file size.
    """
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KiB", "MiB", "GiB", "TiB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
