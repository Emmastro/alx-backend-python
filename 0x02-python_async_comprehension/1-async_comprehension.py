#!/usr/bin/env python3
"""generate a list from a async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect async generated list and return it"""
    result = [i async for i in async_generator()]
    return result
