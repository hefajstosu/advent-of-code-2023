import math
import re
import sys


def steps(start, done, moves, graph):
    node, n = start, 0
    while not done(node):
        node = graph[node][0 if moves[n % len(moves)] == "L" else 1]
        n += 1
    return n


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        moves, body = f.read().strip().split("\n\n")
    moves = moves.strip()
    graph = {}
    for a, b, c in re.findall(r"(\w+) = \((\w+), (\w+)\)", body):
        graph[a] = (b, c)

    part1 = steps("AAA", lambda x: x == "ZZZ", moves, graph) if "AAA" in graph else "-"

    # cykle, wiec NWW
    part2 = 1
    for node in graph:
        if node.endswith("A"):
            n = steps(node, lambda x: x.endswith("Z"), moves, graph)
            part2 = part2 * n // math.gcd(part2, n)
    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


main()
