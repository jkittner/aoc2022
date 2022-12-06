from __future__ import annotations

import argparse
from collections.abc import Sequence

import pytest


def _solve(data: str) -> int:
    data = data.strip()
    left_idx = 0
    right_idx = 14
    while right_idx <= len(data) - 1:
        window = data[left_idx:right_idx]
        if len(set(window)) == 14:
            return right_idx

        left_idx += 1
        right_idx += 1
    else:
        raise AssertionError('past end')


@pytest.mark.parametrize(
    ('s', 'exp'),
    (
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
    ),
)
def test_solve(s, exp):
    assert _solve(s) == exp


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
