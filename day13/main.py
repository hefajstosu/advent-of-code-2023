import sys


def mirror_row(rows, smudges):
    # szukamy odbicia
    for r in range(1, len(rows)):
        diff = 0
        for a, b in zip(rows[r - 1::-1], rows[r:]):
            diff += sum(x != y for x, y in zip(a, b))
            if diff > smudges:
                break
        if diff == smudges:
            return r
    return 0


def score(pattern, smudges):
    cols = ["".join(col) for col in zip(*pattern)]
    return 100 * mirror_row(pattern, smudges) + mirror_row(cols, smudges)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        blocks = f.read().strip().split("\n\n")
    patterns = [b.split("\n") for b in blocks]

    print("Czesc 1:", sum(score(p, 0) for p in patterns))
    print("Czesc 2:", sum(score(p, 1) for p in patterns))


if __name__ == "__main__":
    main()
