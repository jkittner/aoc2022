from __future__ import annotations

import argparse
from collections.abc import Iterable
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')


def threewise(i: Iterable[T]) -> Iterable[tuple[T, T, T]]:
    t = iter(i)
    return zip(t, t, t)


def _solve(data: str) -> int:
    result = 0
    for a, b, c in threewise(data.splitlines()):
        common_item, = set(a) & set(b) & set(c)
        if common_item.islower():
            priority = ord(common_item) - 96
        else:
            priority = ord(common_item) - 38
        result += priority
    return result


TEST_INPUT = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''


def test_solve():
    assert _solve(TEST_INPUT) == 70


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args(argv)
    with open(args.input) as f:
        data = f.read()

    print(f'the solution is: {_solve(data)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
