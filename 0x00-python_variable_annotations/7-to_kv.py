#!/usr/bin/env python3

""""Complex types - string and int/float to tuple"""

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple with str and float memebers'''
    return (k, v * v)
