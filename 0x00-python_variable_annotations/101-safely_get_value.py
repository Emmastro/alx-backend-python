#!/usr/bin/env python3
"""module element length"""


def safely_get_value(dct, key, default = None):
    """safely get value"""
    if key in dct:
        return dct[key]
    else:
        return default
