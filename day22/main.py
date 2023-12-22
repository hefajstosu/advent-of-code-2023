import sys
from collections import deque


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    bricks = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            a, b = line.strip().split("~")
            p, q = list(map(int, a.split(","))), list(map(int, b.split(",")))
            bricks.append(tuple(min(p[i], q[i]) for i in range(3)) + tuple(max(p[i], q[i]) for i in range(3)))
    bricks.sort(key=lambda br: br[2])

    # zrzucamy klocki
    top = {}
    supported_by = [set() for _ in bricks]
    above = [set() for _ in bricks]
    for i, (x1, y1, z1, x2, y2, z2) in enumerate(bricks):
        cells = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        base = max((top[c][0] for c in cells if c in top), default=0) + 1
        height = z2 - z1
        for c in cells:
            if c in top and top[c][0] == base - 1:
                supported_by[i].add(top[c][1])
            top[c] = (base + height, i)
        for j in supported_by[i]:
            above[j].add(i)

    # jedyne podpory
    sole = set()
    for s in supported_by:
        if len(s) == 1:
            sole |= s
    print("Czesc 1:", len(bricks) - len(sole))

    # reakcja lancuchowa
    total = 0
    for i in range(len(bricks)):
        fallen = {i}
        queue = deque([i])
        while queue:
            b = queue.popleft()
            for a in above[b]:
                if a not in fallen and supported_by[a] <= fallen:
                    fallen.add(a)
                    queue.append(a)
        total += len(fallen) - 1
    print("Czesc 2:", total)


main()
