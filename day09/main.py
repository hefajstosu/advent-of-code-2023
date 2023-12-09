import sys


def extrapolate(seq):
    # roznice do zera
    total = 0
    while any(seq):
        total += seq[-1]
        seq = [b - a for a, b in zip(seq, seq[1:])]
    return total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        seqs = [list(map(int, line.split())) for line in f if line.strip()]

    part1 = sum(extrapolate(s) for s in seqs)
    # odwracamy ciag
    part2 = sum(extrapolate(s[::-1]) for s in seqs)

    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


if __name__ == "__main__":
    main()
