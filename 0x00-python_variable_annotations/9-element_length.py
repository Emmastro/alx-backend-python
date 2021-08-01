#!/usr/bin/env python3
"""module element length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """iterate through sequence"""
    return [(i, len(i)) for i in lst]
