#!/usr/bin/env python3

""""Define Variables"""


from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns a sum of floats'''
    return reduce(lambda a, b: a + b, input_list)
