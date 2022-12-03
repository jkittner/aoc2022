from __future__ import annotations

import argparse
from collections.abc import Sequence


def _solve(data: str) -> int:
    result = 0
    for rucksack in data.splitlines():
        first_half = set(rucksack[:len(rucksack)//2])
        second_half = set(rucksack[len(rucksack)//2:])
        in_both, = first_half.intersection(second_half)
        if in_both.islower():
            priority = ord(in_both) - 96
        else:
            priority = ord(in_both) - 38
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
    assert _solve(TEST_INPUT) == 157


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
