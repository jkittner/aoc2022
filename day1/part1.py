from __future__ import annotations

import argparse
from collections.abc import Sequence


def _solve(data: str) -> int:
    result = []
    current = 0
    for cal in data.splitlines():
        if cal != '':
            current += int(cal)
        else:
            result.append(current)
            current = 0
    return max(result)


TEST_INPUT = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''


def test_solve():
    assert _solve(TEST_INPUT) == 24000


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
