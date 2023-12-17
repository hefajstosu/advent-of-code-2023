import heapq
import sys


def solve(grid, min_steps, max_steps):
    h, w = len(grid), len(grid[0])
    # stan Dijkstry
    dist = {}
    heap = [(0, 0, 0, 0), (0, 0, 0, 1)]
    while heap:
        cost, r, c, axis = heapq.heappop(heap)
        if (r, c) == (h - 1, w - 1):
            return cost
        if dist.get((r, c, axis), float("inf")) < cost:
            continue
        # skrecamy zawsze
        dirs = ((1, 0), (-1, 0)) if axis == 0 else ((0, 1), (0, -1))
        for dr, dc in dirs:
            nr, nc, ncost = r, c, cost
            for step in range(1, max_steps + 1):
                nr += dr
                nc += dc
                if not (0 <= nr < h and 0 <= nc < w):
                    break
                ncost += grid[nr][nc]
                if step >= min_steps:
                    key = (nr, nc, 1 - axis)
                    if ncost < dist.get(key, float("inf")):
                        dist[key] = ncost
                        heapq.heappush(heap, (ncost, nr, nc, 1 - axis))
    return -1


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        grid = [[int(ch) for ch in line.strip()] for line in f if line.strip()]
    print("Czesc 1:", solve(grid, 1, 3))
    print("Czesc 2:", solve(grid, 4, 10))


main()
