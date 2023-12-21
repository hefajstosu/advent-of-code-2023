# jak odpalic
import sys
from collections import deque


def distances(grid, start, limit, infinite):
    # BFS z modulo
    h, w = len(grid), len(grid[0])
    dist = {start: 0}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        d = dist[(r, c)]
        if d == limit:
            continue
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if (nr, nc) in dist:
                continue
            if not infinite and not (0 <= nr < h and 0 <= nc < w):
                continue
            if grid[nr % h][nc % w] == "#":
                continue
            dist[(nr, nc)] = d + 1
            queue.append((nr, nc))
    return dist


def reachable(dist, steps):
    # ta sama parzystosc
    return sum(1 for d in dist.values() if d <= steps and d % 2 == steps % 2)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        grid = [line.strip() for line in f if line.strip()]
    start = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")
    n = len(grid)

    if len(sys.argv) > 2:
        steps = int(sys.argv[2])
        print("Kroki", steps, "na nieskonczonej siatce:", reachable(distances(grid, start, steps, True), steps))
        return

    # przyklad czy input
    example = n < 50
    steps1 = 6 if example else 64
    print("Czesc 1:", reachable(distances(grid, start, steps1, False), steps1))

    if example:
        # tylko prawdziwy input
        print("Czesc 2: -")
        return

    # dopasowanie kwadratowe
    target = 26501365
    rem = target % n
    dist = distances(grid, start, rem + 2 * n, True)
    a0, a1, a2 = (reachable(dist, rem + i * n) for i in range(3))
    x = target // n
    print("Czesc 2:", a0 + x * (a1 - a0) + x * (x - 1) // 2 * (a2 - 2 * a1 + a0))


main()
