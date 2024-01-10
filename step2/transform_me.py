import typing
from typing import Optional


def square_maybe(x: Optional[int]) -> int:
    return x * 2 if x else None


def square_tuple_maybe(x: typing.Optional[tuple[int, int]]) -> tuple[int, int]:
    return (x[0] * 2, x[1] * 2) if x else None
