#!/usr/bin/env python3


def is_even(x):
    return not (x % 2)


print(tuple(filter(is_even, range(10))))
# (0, 2, 4, 6, 8)


def double(x):
    return x * 2


print(tuple(map(double, range(5))))
# (0, 2, 4, 6, 8)


import functools


def add(a, b):
    return a + b


print(functools.reduce(add, range(5)))
# 10


from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    name: str

print(Point(4, 5, 'my point'))
# Point(x=4, y=5, name='my point')
