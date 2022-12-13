from __future__ import annotations

import argparse
import os
from collections.abc import Sequence


def _solve(data: str) -> int:
    all_dirs: dict[str, int] = {}
    all_files: dict[str, str] = {}

    # maybe we always start at root?
    cur_dir = '/'
    for log in data.splitlines():
        # back to previous dir
        if log == '$ cd ..':
            cur_dir = os.path.dirname(cur_dir) or '/'
        # change directory
        elif log.startswith('$ cd'):
            cur_dir = os.path.join(cur_dir, log.split()[-1])
        elif not log.startswith(('dir', '$ ls')):
            f_size, f_name, = log.split()
            all_files[os.path.join(cur_dir, f_name)] = f_size

        # set size to 0 as a placeholder for now
        all_dirs[cur_dir] = 0

    for name, size in all_files.items():
        for d in all_dirs:
            if name.startswith(d):
                all_dirs[d] += int(size)

    return sum(s for s in all_dirs.values() if s <= 100000)


TEST_INPUT = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''


def test_solve():
    assert _solve(TEST_INPUT) == 95437


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
