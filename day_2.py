#!/usr/bin/env python3

RGB_FILTER = (12, 13, 14)

if __name__ == '__main__':
    rf, gf, bf = RGB_FILTER

    with open('content/day_2.txt', 'r') as f:

        w = [
            (n, (
                max([int(i) for i, col in c if col == 'red']),
                max([int(i) for i, col in c if col == 'green']),
                max([int(i) for i, col in c if col == 'blue']),
            ))
            for n, c in (
                (
                    int(g.split(' ')[1]),
                    [
                        tuple(y.strip().split(' '))
                        for x in d.split(';')
                        for y in x.strip().split(',')
                    ]
                ) for [g, d] in
                (
                    x.split(':')
                    for x in f.readlines()
                )
            )
        ]

    print(
        'part 1',
        sum([
            n for n, (r, g, b) in w
            if r <= rf and g <= gf and b <= bf
        ])
    )

    print(
        'part 2',
        sum([
            r * g * b for _, (r, g, b) in w
        ])
    )
