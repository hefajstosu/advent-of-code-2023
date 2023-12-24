import sys
from fractions import Fraction


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def solve_linear(m, rhs):
    # Gauss na ulamkach
    n = len(m)
    a = [[Fraction(x) for x in row] + [Fraction(r)] for row, r in zip(m, rhs)]
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        if piv is None:
            return None
        a[col], a[piv] = a[piv], a[col]
        for r in range(n):
            if r != col and a[r][col] != 0:
                f = a[r][col] / a[col][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return [a[i][n] / a[i][i] for i in range(n)]


def part1(stones, lo, hi):
    count = 0
    for i in range(len(stones)):
        (x1, y1, _), (vx1, vy1, _) = stones[i]
        for j in range(i + 1, len(stones)):
            (x2, y2, _), (vx2, vy2, _) = stones[j]
            det = vx1 * vy2 - vy1 * vx2
            if det == 0:
                continue  # rownolegle
            # rownanie przeciecia
            t = Fraction((x2 - x1) * vy2 - (y2 - y1) * vx2, det)
            s = Fraction((x2 - x1) * vy1 - (y2 - y1) * vx1, det)
            if t < 0 or s < 0:
                continue  # bylo w przeszlosci
            px, py = x1 + t * vx1, y1 + t * vy1
            if lo <= px <= hi and lo <= py <= hi:
                count += 1
    return count


def part2(stones):
    # odejmujemy rownania
    def rows(i, j):
        (pi, vi), (pj, vj) = stones[i], stones[j]
        dv = [vi[k] - vj[k] for k in range(3)]
        dp = [pi[k] - pj[k] for k in range(3)]
        ci, cj = cross(pi, vi), cross(pj, vj)
        c = [ci[k] - cj[k] for k in range(3)]
        m = [
            [0, dv[2], -dv[1], 0, -dp[2], dp[1]],
            [-dv[2], 0, dv[0], dp[2], 0, -dp[0]],
            [dv[1], -dv[0], 0, -dp[1], dp[0], 0],
        ]
        return m, c

    n = len(stones)
    for a in range(1, n):
        for b in range(a + 1, n):
            m1, c1 = rows(0, a)
            m2, c2 = rows(0, b)
            sol = solve_linear(m1 + m2, c1 + c2)
            if sol is not None:
                return int(sol[0] + sol[1] + sol[2])
    return None


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    stones = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            p, v = line.split("@")
            stones.append((tuple(int(x) for x in p.split(",")), tuple(int(x) for x in v.split(","))))
    # przyklad czy input
    example = max(abs(c) for p, _ in stones for c in p) < 1000
    lo, hi = (7, 27) if example else (200000000000000, 400000000000000)
    print("Czesc 1:", part1(stones, lo, hi))
    print("Czesc 2:", part2(stones))


main()
