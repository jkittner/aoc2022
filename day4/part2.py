from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


SECTION_PATTERN = re.compile(r'(\d{1,2})\-(\d{1,2}),(\d{1,2})\-(\d{1,2})')


def _solve(data: str) -> int:
    counter = 0
    for row in data.splitlines():
        a_start, a_end, b_start, b_end = SECTION_PATTERN.findall(row)[0]
        # b over a
        if int(b_start) >= int(a_start) and int(b_start) <= int(a_end):
            counter += 1
        # b below a
        elif int(a_start) >= int(b_start) and int(a_start) <= int(b_end):
            counter += 1

    return counter


TEST_INPUT = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''


def test_solve():
    assert _solve(TEST_INPUT) == 4


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
