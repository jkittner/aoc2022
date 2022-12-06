from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

STACK_PATTERN = re.compile(r'( {3}|[A-Z])')
INSTRUCTION_PATTERN = re.compile(r'move (\d+) from (\d+) to (\d+)')


def _solve(data: str) -> str:
    data_rows = data.splitlines()
    stack_plan = []
    instructions = []
    for data_row in data_rows:
        stack = STACK_PATTERN.findall(data_row)
        instruction = INSTRUCTION_PATTERN.findall(data_row)
        if stack:
            stack_plan.append(stack)
        if instruction:
            instructions.append(
                [int(i) for i in instruction[0] if not i.isspace()],
            )

    # last row is index number rows
    del stack_plan[-1]
    # create transpose skeleton
    stack_plan_transposed: list[list[str]] = [
        [] for _ in range(len(stack_plan[-1]))
    ]
    stack_plan.reverse()

    for row in stack_plan:
        for idx, element in enumerate(row):
            if not element.isspace():
                stack_plan_transposed[idx].append(element)

    for nr, src, dest in instructions:
        current_stack = stack_plan_transposed[src - 1][-nr:]
        del stack_plan_transposed[src - 1][-nr:]
        stack_plan_transposed[dest - 1].extend(current_stack)

    return ''.join([i[-1] for i in stack_plan_transposed])


TEST_INPUT = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''  # noqa: W291


def test_solve():
    assert _solve(TEST_INPUT) == 'MCD'


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
