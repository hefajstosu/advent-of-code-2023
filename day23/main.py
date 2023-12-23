import sys

SLOPES = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}


def build_graph(grid, slopes):
    # kompresujemy do grafu
    h, w = len(grid), len(grid[0])
    start = (0, grid[0].index("."))
    end = (h - 1, grid[h - 1].index("."))

    def neighbors(r, c):
        ch = grid[r][c]
        if slopes and ch in SLOPES:
            dirs = [SLOPES[ch]]
        else:
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "#":
                yield nr, nc

    nodes = {start, end}
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "#":
                continue
            cnt = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "#":
                    cnt += 1
            if cnt >= 3:
                nodes.add((r, c))

    edges = {n: {} for n in nodes}
    for node in nodes:
        stack = [(node, 0)]
        seen = {node}
        while stack:
            (r, c), d = stack.pop()
            if d > 0 and (r, c) in nodes:
                edges[node][(r, c)] = max(edges[node].get((r, c), 0), d)
                continue
            for nb in neighbors(r, c):
                if nb not in seen:
                    seen.add(nb)
                    stack.append((nb, d + 1))
    return start, end, edges


def longest(start, end, edges):
    index = {n: i for i, n in enumerate(edges)}
    adj = [[] for _ in edges]
    for n, targets in edges.items():
        for t, d in targets.items():
            adj[index[n]].append((index[t], 1 << index[t], d))
    s, e = index[start], index[end]

    # skrot do konca
    into_end = [i for i in range(len(adj)) if any(t == e for t, _, _ in adj[i])]
    extra = 0
    if len(into_end) == 1 and into_end[0] != s:
        last = into_end[0]
        extra = next(d for t, _, d in adj[last] if t == e)
        e = last

    best = -1
    stack = [(s, 1 << s, 0)]
    while stack:
        node, mask, d = stack.pop()
        if node == e:
            if d > best:
                best = d
            continue
        for t, bit, w in adj[node]:
            if not mask & bit:
                stack.append((t, mask | bit, d + w))
    return best + extra if best >= 0 else -1


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        grid = [line.strip() for line in f if line.strip()]
    print("Czesc 1:", longest(*build_graph(grid, True)))
    print("Czesc 2:", longest(*build_graph(grid, False)))


main()
