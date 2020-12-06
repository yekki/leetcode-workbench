from typing import List
from common import timeit


def _b_search_1(alist: List, item: int) -> bool:
    if len(alist) == 0:
        return False

    mid = len(alist) // 2
    if item == alist[mid]:
        return True
    elif item < alist[mid]:
        return _b_search_1(alist[:mid], item)
    else:
        return _b_search_1(alist[mid + 1:], item)


@timeit
def b_search_1(alist: List, item: int):
    return _b_search_1(alist, item)


@timeit
def b_search_2(alist: List, item: int) -> bool:

    if alist is None:
        return False
    
    size = len(alist)

    if size == 0:
        return False

    first, last = 0, size - 1

    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    else:
        return False


@timeit
def s_search(alist: List, item: int) -> bool:
    if alist is None:
        return 0

    for i in alist:
        if i == item:
            return True
    else:
        return False


if __name__ == '__main__':
    params = ([5, 10, 15, 18, 35, 55, 65, 75, 99], 18)
    b_search_1(*params)
    b_search_2(*params)
    s_search(*params)