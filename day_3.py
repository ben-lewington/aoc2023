#!/usr/bin/env python3

CHECK_CODE_OFFSETS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

if __name__ == "__main__":
    with open('content/day_3.txt', 'r') as f:
        d = f.readlines()

    codes = {}
    for r, line in enumerate(d):
        field_iter = enumerate(line)
        codes[r] = {}
        for c, ch in field_iter:
            if not ch.isdigit():
                continue
            code = ch
            ce = c
            td = '.'
            while True:
                try:
                    ce, td = next(field_iter)
                except StopIteration:
                    break

                if td.isdigit():
                    code += td
                    continue
                else:
                    codes[r][(c, ce - 1)] = int(code)
                    break

    valid = {}
    for r, line in enumerate(d):
        for c, ch in enumerate(line):
            if ch == '\n':
                break
            elif ch == '.' or ch.isdigit():
                continue

            for ri, ci in CHECK_CODE_OFFSETS:
                rc = codes.get(r + ri, None)
                if not rc:
                    continue

                for (ccs, cce), value in rc.items():
                    if ccs <= c + ci and c + ci <= cce:
                        valid[(r + ri, ccs)] = value

    gears = {}
    for r, line in enumerate(d):
        for c, ch in enumerate(line):
            if not ch == '*':
                continue

            neighbours = {}

            for ri, ci in CHECK_CODE_OFFSETS:
                rc = codes.get(r + ri, None)
                if not rc:
                    continue

                for (ccs, cce), value in rc.items():
                    if ccs <= c + ci and c + ci <= cce:
                        neighbours[(r + ri, ccs)] = value

            if len(neighbours) == 2:
                p = 1
                for v in neighbours.values():
                    p *= v

                gears[(r, c)] = p



    print('Part 1', sum(valid.values()))
    print('Part 2', sum(gears.values()))
