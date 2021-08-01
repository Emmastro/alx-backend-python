#!/usr/bin/env python3
"""module element length"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe first element"""
    if lst:
        return lst[0]
    else:
        return None
