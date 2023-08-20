#!/usr/bin/env python3

""""Complex types - mixed list"""


from functools import reduce
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    '''Returns a sum of floats and int args'''
    return reduce(lambda a, b: a + b, mxd_lst)
