import sys
from functools import lru_cache


def arrangements(s, groups):
    n, m = len(s), len(groups)

    @lru_cache(maxsize=None)
    def f(i, j):
        # pozycja i grupa
        if i >= n:
            return 1 if j == m else 0
        res = 0
        ch = s[i]
        if ch in ".?":
            res += f(i + 1, j)
        if ch in "#?" and j < m:
            g = groups[j]
            # czy grupa pasuje
            if i + g <= n and "." not in s[i:i + g] and (i + g == n or s[i + g] != "#"):
                res += f(i + g + 1, j + 1)
        return res

    return f(0, 0)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    rows = []
    with open(path) as f:
        for line in f:
            if line.strip():
                s, g = line.split()
                rows.append((s, tuple(map(int, g.split(",")))))

    part1 = sum(arrangements(s, g) for s, g in rows)
    # razy piec
    part2 = sum(arrangements("?".join([s] * 5), g * 5) for s, g in rows)

    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


if __name__ == "__main__":
    main()
