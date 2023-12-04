import sys


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    matches = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            nums = line.split(":")[1]
            win, have = nums.split("|")
            matches.append(len(set(win.split()) & set(have.split())))
    part1 = sum(1 << (m - 1) for m in matches if m > 0)
    # liczymy kopie
    copies = [1] * len(matches)
    for i, m in enumerate(matches):
        for j in range(i + 1, min(i + 1 + m, len(matches))):
            copies[j] += copies[i]
    print("Czesc 1:", part1)
    print("Czesc 2:", sum(copies))


main()
