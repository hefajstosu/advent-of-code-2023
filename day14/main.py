import sys


def tilt_north(grid):
    h, w = len(grid), len(grid[0])
    for c in range(w):
        free = 0
        for r in range(h):
            ch = grid[r][c]
            if ch == "#":
                free = r + 1
            elif ch == "O":
                if free != r:
                    grid[free][c] = "O"
                    grid[r][c] = "."
                free += 1


def rotate_cw(grid):
    # obracamy w prawo
    return [list(row) for row in zip(*grid[::-1])]


def load(grid):
    h = len(grid)
    return sum(h - r for r, row in enumerate(grid) for ch in row if ch == "O")


def spin_cycle(grid):
    # pelny cykl
    for _ in range(4):
        tilt_north(grid)
        grid = rotate_cw(grid)
    return grid


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        start = [list(line.rstrip("\n")) for line in f if line.strip()]

    grid = [row[:] for row in start]
    tilt_north(grid)
    part1 = load(grid)

    # szukamy cyklu
    total = 1000000000
    grid = [row[:] for row in start]
    seen = {}
    history = []
    i = 0
    while True:
        key = "".join("".join(row) for row in grid)
        if key in seen:
            first = seen[key]
            period = i - first
            idx = first + (total - first) % period
            part2 = history[idx]
            break
        seen[key] = i
        history.append(load(grid))
        grid = spin_cycle(grid)
        i += 1

    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


if __name__ == "__main__":
    main()
