#!/usr/bin/env python3
""" generate swapped list of float """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """generate return value of wait_random"""
    returned_value = [wait_random(max_delay) for i in range(n)]
    returned_value = asyncio.as_completed(returned_value)
    returned_value = [await i for i in returned_value]
    return returned_value
