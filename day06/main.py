import math
import sys


def ways(t, d):
    # rownanie kwadratowe
    delta = t * t - 4 * d
    if delta <= 0:
        return 0
    r = math.isqrt(delta)
    lo = max(0, (t - r) // 2 - 1)
    while lo * (t - lo) <= d:
        lo += 1
    hi = min(t, (t + r) // 2 + 1)
    while hi * (t - hi) <= d:
        hi -= 1
    return max(0, hi - lo + 1)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        lines = [l for l in f if l.strip()]
    times = lines[0].split(":")[1].split()
    dists = lines[1].split(":")[1].split()
    part1 = 1
    for t, d in zip(times, dists):
        part1 *= ways(int(t), int(d))
    part2 = ways(int("".join(times)), int("".join(dists)))
    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


main()
