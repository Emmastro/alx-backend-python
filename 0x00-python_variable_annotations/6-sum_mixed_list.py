#!/usr/bin/env python3
"""This module contains modules to perform sum of lists"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """perform addition of a mixed list"""
    return sum(mxd_lst)
