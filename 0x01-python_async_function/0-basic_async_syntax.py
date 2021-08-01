#!/usr/bin/env python3
""" creat a coroutine function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for a random number """
    number = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
