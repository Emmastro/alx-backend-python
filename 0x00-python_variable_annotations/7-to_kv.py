#!/usr/bin/env python3
"""module to perform some actions"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple"""
    return (k, pow(v, 2))
