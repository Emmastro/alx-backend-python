#!/usr/bin/env python3
""" create new tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return list of values"""
    returned_value = [task_wait_random(max_delay) for i in range(n)]
    newList = []
    for i in asyncio.as_completed(returned_value):
        newList.append(await i)
    return newList
