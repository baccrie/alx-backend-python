#!/usr/bin/env python3

""""Complex types - functions"""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns wahala'''
    return [(i, len(i)) for i in lst]
