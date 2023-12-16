import sys

# kierunki
DR = (0, 1, 0, -1)
DC = (1, 0, -1, 0)
# odbicia promienia
NEXT = {
    ".": ((0,), (1,), (2,), (3,)),
    "/": ((3,), (2,), (1,), (0,)),
    "\\": ((1,), (0,), (3,), (2,)),
    "|": ((1, 3), (1,), (1, 3), (3,)),
    "-": ((0,), (0, 2), (2,), (0, 2)),
}


def energized(grid, sr, sc, sd):
    h, w = len(grid), len(grid[0])
    seen = bytearray(h * w * 4)
    stack = [(sr, sc, sd)]
    while stack:
        r, c, d = stack.pop()
        if not (0 <= r < h and 0 <= c < w):
            continue
        k = (r * w + c) * 4 + d
        if seen[k]:
            continue
        seen[k] = 1
        for nd in NEXT[grid[r][c]][d]:
            stack.append((r + DR[nd], c + DC[nd], nd))
    return sum(1 for i in range(h * w) if any(seen[i * 4:i * 4 + 4]))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]
    h, w = len(grid), len(grid[0])

    part1 = energized(grid, 0, 0, 0)

    # wszystkie wejscia
    starts = []
    for r in range(h):
        starts.append((r, 0, 0))
        starts.append((r, w - 1, 2))
    for c in range(w):
        starts.append((0, c, 1))
        starts.append((h - 1, c, 3))
    part2 = max(energized(grid, *s) for s in starts)

    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


if __name__ == "__main__":
    main()
