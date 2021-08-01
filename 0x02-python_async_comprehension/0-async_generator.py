#!/usr/bin/env python3
""" Module to generate asynchronus list comprehension"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generate asyncronisly """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
