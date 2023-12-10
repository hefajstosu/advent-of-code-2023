import sys

# polaczenia rur
DIRS = {
    "|": {(-1, 0), (1, 0)},
    "-": {(0, -1), (0, 1)},
    "L": {(-1, 0), (0, 1)},
    "J": {(-1, 0), (0, -1)},
    "7": {(1, 0), (0, -1)},
    "F": {(1, 0), (0, 1)},
}


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        grid = [list(line.rstrip("\n")) for line in f if line.strip()]
    h, w = len(grid), len(grid[0])

    sr, sc = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == "S")

    # zgadujemy S
    conn = set()
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = sr + dr, sc + dc
        if 0 <= r < h and 0 <= c < w and (-dr, -dc) in DIRS.get(grid[r][c], ()):
            conn.add((dr, dc))
    grid[sr][sc] = next(ch for ch, d in DIRS.items() if d == conn)

    # lecimy petla
    loop = {(sr, sc)}
    prev = None
    r, c = sr, sc
    while True:
        for dr, dc in DIRS[grid[r][c]]:
            nxt = (r + dr, c + dc)
            if nxt != prev:
                break
        prev = (r, c)
        r, c = nxt
        if (r, c) == (sr, sc):
            break
        loop.add((r, c))

    part1 = len(loop) // 2

    # parzystosc przeciec
    part2 = 0
    for r in range(h):
        inside = False
        for c in range(w):
            if (r, c) in loop:
                if grid[r][c] in "|LJ":
                    inside = not inside
            elif inside:
                part2 += 1

    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


if __name__ == "__main__":
    main()
