import sys


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    limit = {"red": 12, "green": 13, "blue": 14}
    part1 = part2 = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            head, rest = line.split(":")
            game_id = int(head.split()[1])
            # max kostek
            best = {"red": 0, "green": 0, "blue": 0}
            for draw in rest.split(";"):
                for item in draw.split(","):
                    n, color = item.split()
                    best[color] = max(best[color], int(n))
            if all(best[c] <= limit[c] for c in limit):
                part1 += game_id
            part2 += best["red"] * best["green"] * best["blue"]
    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


main()
