
if __name__ == "__main__":
    with open('content/day_4.txt', 'r') as f:
        d = f.read()

    f = [
        x for x in d.split('\n') if len(x) > 0
    ]

    scores = {}
    num_offs = {}
    for l in f:
        [id, p] = l.split(':')

        id = int(id.strip().split(' ')[-1])

        [pw, pa] = p.strip().split('|')

        pw = {int(x) for x in pw.split(' ') if len(x) > 0}
        pa = {int(x) for x in pa.split(' ') if len(x) > 0}

        win_v = pw.intersection(pa)

        if len(win_v) == 0:
            scores[id] = 0
        else:
            scores[id] = 2 ** (len(win_v) - 1)

        num_offs[id] = (1, len(win_v))

    print('Part 1', sum(scores.values()))

    for id in num_offs.keys():
        card_count, win_count = num_offs[id]

        for j in range(win_count):
            a, b = num_offs[id + j + 1]

            num_offs[id + j + 1] = (a + card_count, b)

        # print(id, card_count, win_count)

    print('Part 2', sum([x for x, _ in num_offs.values()]))
