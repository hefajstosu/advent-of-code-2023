import sys
from collections import deque


def bfs_path(graph, flow, s, t):
    # szukamy sciezki
    prev = {s: None}
    queue = deque([s])
    while queue:
        u = queue.popleft()
        if u == t:
            break
        for v in graph[u]:
            if v not in prev and flow.get((u, v), 0) < 1:
                prev[v] = u
                queue.append(v)
    return prev


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    graph = {}
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            a, rest = line.split(":")
            for b in rest.split():
                graph.setdefault(a, set()).add(b)
                graph.setdefault(b, set()).add(a)

    nodes = sorted(graph)
    s = nodes[0]
    # max przeplyw 3
    for t in nodes[1:]:
        flow = {}
        paths = 0
        while True:
            prev = bfs_path(graph, flow, s, t)
            if t not in prev:
                break
            paths += 1
            if paths > 3:
                break
            v = t
            while prev[v] is not None:
                u = prev[v]
                flow[(u, v)] = flow.get((u, v), 0) + 1
                flow[(v, u)] = flow.get((v, u), 0) - 1
                v = u
        if paths == 3:
            # jedna polowa
            size = len(prev)
            print("Czesc 1:", size * (len(nodes) - size))
            print("Czesc 2: -")
            return
    print("Czesc 1: brak ciecia na 3 krawedziach")
    print("Czesc 2: -")


main()
