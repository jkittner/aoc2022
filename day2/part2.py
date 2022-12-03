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
    'X': 'loose',
    'Y': 'draw',
    'Z': 'win',
}
WINS = {
    'rock': 'scissor',
    'scissor': 'paper',
    'paper': 'rock',
}
LOSES = {
    'scissor': 'rock',
    'paper': 'scissor',
    'rock': 'paper',
}


def _play_round(opponent, myself) -> int:
    opponent_trans = INSTRUCTION_MAPPING[opponent]
    ldw = INSTRUCTION_MAPPING[myself]
    # we need to win
    if ldw == 'win':
        to_be_played = LOSES[opponent_trans]
        score = 6
    # we need to draw
    elif ldw == 'draw':
        to_be_played = opponent_trans
        score = 3
    # we need to loose
    else:
        to_be_played = WINS[opponent_trans]
        score = 0

    return POINTS[to_be_played] + score


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
    assert _solve(TEST_INPUT) == 12


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
