#!/usr/bin/env python3

""""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''A funtion that returns a function that accepts float'''
    return lambda a: a * multiplier
