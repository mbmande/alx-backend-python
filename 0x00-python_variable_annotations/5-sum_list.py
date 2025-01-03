#!/usr/bin/env python3

"""-=======================================
"""
 

from typing import List


def sum_list(input_list: List[float]) -> float:
    """============================
    """
    sum = 0.0

    for num in input_list:
        if isinstance(num, float):  # if type(num) is float:
            sum += num

    return sum
