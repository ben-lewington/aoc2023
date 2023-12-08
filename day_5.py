from dataclasses import dataclass


@dataclass
class Map:
    dst_rng_start: int
    src_rng_start: int
    rng_len: int

    def in_src_range(self, src_index: int):
        return src_index - self.src_rng_start in range(self.rng_len)


def make_map_from(input: str) -> list[Map]:
    return [
        Map(*[
            int(y) for y in x.split(' ')
        ])
        for x in input.split('\n')
        if not ':' in x and len(x) > 0
    ]


def resolve_from(
    seeds: list[int],
    prev_resolver: dict[int, int] | None,
    mapper: list[Map]
) -> dict[int, int]:
    resolver = {}

    for s in seeds:
        if prev_resolver is None:
            l = s
        else:
            l = prev_resolver[s]

        for m in mapper:
            if m.in_src_range(l):
                resolver[s] = m.dst_rng_start + (l - m.src_rng_start)

                break

        if s not in resolver:
            resolver[s] = l

    return resolver


if __name__ == "__main__":
    with open('content/day_5.txt', 'r') as f:
        d = f.read()

    it = iter(d.split('\n\n'))

    seeds = [int(x) for x in next(it).split(':', maxsplit=2)[-1].strip().split(' ')]

    resolver, prev_resolver = {}, None
    for data in it:
        resolver = resolve_from(seeds, prev_resolver, make_map_from(data))

        prev_resolver = resolver

    print('Part 1:', min(resolver.values()))

    it = iter(d.split('\n\n'))

    seed_it = iter(next(it).split(':', maxsplit=2)[-1].strip().split(' '))

    seeds = []
    for s in seed_it:
        seeds.append((int(s), int(next(seed_it))))

    print(seeds)

    #
    #   a -> a + l
    #   b -> b + m
    #

    resolver, prev_resolver = {}, None
    for data in it:
        mapper = make_map_from(data)

        for seed_start, seed_len in seeds:
            print(seed_start, seed_len)

