# jak odpalic
import sys


def total_distance(galaxies, empty_rows, empty_cols, factor):
    # rozciagamy puste
    def expand(v, empty):
        return v + sum(1 for e in empty if e < v) * (factor - 1)

    pts = [(expand(r, empty_rows), expand(c, empty_cols)) for r, c in galaxies]
    total = 0
    for i in range(len(pts)):
        r1, c1 = pts[i]
        for j in range(i + 1, len(pts)):
            r2, c2 = pts[j]
            total += abs(r1 - r2) + abs(c1 - c2)
    return total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    factor2 = int(sys.argv[2]) if len(sys.argv) > 2 else 1000000
    with open(path) as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]

    galaxies = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]
    empty_rows = [r for r, row in enumerate(grid) if "#" not in row]
    empty_cols = [c for c in range(len(grid[0])) if all(row[c] != "#" for row in grid)]

    print("Czesc 1:", total_distance(galaxies, empty_rows, empty_cols, 2))
    print("Czesc 2:", total_distance(galaxies, empty_rows, empty_cols, factor2))


if __name__ == "__main__":
    main()
