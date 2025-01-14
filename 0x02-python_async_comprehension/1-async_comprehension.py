#!/usr/bin/env python3

"""=============-==============-==========
"""
import asyncio
from random import uniform
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """========-==============-=================
    """
    return [i async for i in async_generator()]
