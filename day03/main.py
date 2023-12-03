import sys
from collections import defaultdict


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        grid = [l.rstrip("\n") for l in f if l.strip()]
    h = len(grid)
    part1 = 0
    gears = defaultdict(list)  # gwiazdki -> liczby
    for r in range(h):
        row = grid[r]
        c = 0
        while c < len(row):
            if not row[c].isdigit():
                c += 1
                continue
            start = c
            while c < len(row) and row[c].isdigit():
                c += 1
            num = int(row[start:c])
            # zbieramy symbole
            symbols = set()
            for rr in range(r - 1, r + 2):
                if not 0 <= rr < h:
                    continue
                for cc in range(start - 1, c + 1):
                    if 0 <= cc < len(grid[rr]):
                        ch = grid[rr][cc]
                        if ch != "." and not ch.isdigit():
                            symbols.add((rr, cc, ch))
            if symbols:
                part1 += num
            for rr, cc, ch in symbols:
                if ch == "*":
                    gears[(rr, cc)].append(num)
    part2 = sum(v[0] * v[1] for v in gears.values() if len(v) == 2)
    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


main()
