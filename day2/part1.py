from __future__ import annotations

import argparse
from collections.abc import Sequence

POINTS = {
    'rock': 1,
    'paper': 2,
    'scissor': 3,
}

INSTRUCTION_MAPPING = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissor',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissor',
}
WINS = {
    'rock': 'scissor',
    'scissor': 'paper',
    'paper': 'rock',
}


def _play_round(opponent, myself) -> int:
    opponent_trans = INSTRUCTION_MAPPING[opponent]
    myself_trans = INSTRUCTION_MAPPING[myself]
    # id we win?
    if WINS[myself_trans] == opponent_trans:
        score = 6
    # draw
    elif opponent_trans == myself_trans:
        score = 3
    # we lost
    else:
        score = 0

    return POINTS[myself_trans] + score


def _solve(data: str) -> int:
    score = 0
    for round in data.splitlines():
        opponent, myself = round.split()
        round_score = _play_round(opponent=opponent, myself=myself)
        score += round_score

    return score


TEST_INPUT = '''\
A Y
B X
C Z
'''


def test_solve():
    assert _solve(TEST_INPUT) == 15


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
