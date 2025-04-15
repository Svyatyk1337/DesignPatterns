from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Callable

def totalValues(values: List[int]) -> int:
    result: int = 0
    for value in values:
        result += value
    return result

def totalAllEvenValues(values: List[int]) -> int:
    result: int = 0
    for value in values:
        if value % 2 == 0:
            result += value
    return result

def totalAllValues(values: List[int], filter: Callable[[int], bool]) -> int:
    result: int = 0
    for value in values:
        if filter(value):
            result += value
    return result

def isEven(value: int) -> bool:
    return value % 2 == 0

if __name__ == "__main__":
    values: List[int] = [1, 2, 3, 4, 5]
    print(totalValues(values))
    print(totalAllEvenValues(values))
    print(totalAllValues(values, isEven))
    print(totalAllValues(values, lambda value: value % 2 == 0))
    

