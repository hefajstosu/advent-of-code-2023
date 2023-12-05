import sys


def apply_ranges(ranges, mapping):
    # mapujemy przedzialy
    result = []
    todo = list(ranges)
    while todo:
        s, e = todo.pop()
        for dst, src, ln in mapping:
            lo, hi = max(s, src), min(e, src + ln)
            if lo < hi:
                # tniemy przedzial
                result.append((lo - src + dst, hi - src + dst))
                if s < lo:
                    todo.append((s, lo))
                if hi < e:
                    todo.append((hi, e))
                break
        else:
            result.append((s, e))
    return result


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        blocks = f.read().strip().split("\n\n")
    seeds = list(map(int, blocks[0].split(":")[1].split()))
    maps = []
    for block in blocks[1:]:
        lines = block.strip().split("\n")[1:]
        maps.append([tuple(map(int, l.split())) for l in lines])

    def lowest(ranges):
        for m in maps:
            ranges = apply_ranges(ranges, m)
        return min(s for s, _ in ranges)

    part1 = lowest([(s, s + 1) for s in seeds])
    part2 = lowest([(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)])
    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


main()
