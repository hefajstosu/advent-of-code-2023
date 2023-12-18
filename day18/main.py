import sys

DIRS = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}


def area(moves):
    # shoelace plus Pick
    r = c = 0
    twice = 0
    perimeter = 0
    for d, n in moves:
        dr, dc = DIRS[d]
        nr, nc = r + dr * n, c + dc * n
        twice += r * nc - nr * c
        perimeter += n
        r, c = nr, nc
    return abs(twice) // 2 + perimeter // 2 + 1


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    moves1, moves2 = [], []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            d, n, color = line.split()
            moves1.append((d, int(n)))
            hexpart = color.strip("()#")
            # dekodujemy hexa
            moves2.append(("RDLU"[int(hexpart[5])], int(hexpart[:5], 16)))
    print("Czesc 1:", area(moves1))
    print("Czesc 2:", area(moves2))


main()
