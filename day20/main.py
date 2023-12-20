import sys
from collections import deque
from math import gcd


def parse(lines):
    kinds, outputs = {}, {}
    for line in lines:
        src, dst = line.split(" -> ")
        targets = [t.strip() for t in dst.split(",")]
        if src[0] in "%&":
            kinds[src[1:]] = src[0]
            outputs[src[1:]] = targets
        else:
            kinds[src] = "b"
            outputs[src] = targets
    return kinds, outputs


class Machine:
    def __init__(self, kinds, outputs):
        self.kinds = kinds
        self.outputs = outputs
        self.flip = {m: False for m, k in kinds.items() if k == "%"}
        # pamiec koniunkcji
        self.memory = {m: {} for m, k in kinds.items() if k == "&"}
        for src, targets in outputs.items():
            for t in targets:
                if t in self.memory:
                    self.memory[t][src] = False

    def press(self, watch=None):
        # liczymy impulsy
        low = high = 0
        seen_high = set()
        queue = deque([("button", "broadcaster", False)])
        while queue:
            src, dst, pulse = queue.popleft()
            if pulse:
                high += 1
                if dst == watch:
                    seen_high.add(src)
            else:
                low += 1
            kind = self.kinds.get(dst)
            if kind is None:
                continue
            if kind == "b":
                out = pulse
            elif kind == "%":
                if pulse:
                    continue
                self.flip[dst] = not self.flip[dst]
                out = self.flip[dst]
            else:
                mem = self.memory[dst]
                mem[src] = pulse
                out = not all(mem.values())
            for t in self.outputs[dst]:
                queue.append((dst, t, out))
        return low, high, seen_high


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]
    kinds, outputs = parse(lines)

    m = Machine(kinds, outputs)
    lows = highs = 0
    for _ in range(1000):
        lo, hi, _ = m.press()
        lows += lo
        highs += hi
    print("Czesc 1:", lows * highs)

    # cykle, potem NWW
    feeders = [src for src, targets in outputs.items() if "rx" in targets]
    if len(feeders) != 1 or kinds.get(feeders[0]) != "&":
        print("Czesc 2: -")
        return
    hub = feeders[0]
    inputs = [src for src, targets in outputs.items() if hub in targets]
    cycles = {}
    m = Machine(kinds, outputs)
    presses = 0
    while len(cycles) < len(inputs):
        presses += 1
        _, _, seen = m.press(watch=hub)
        for src in seen:
            cycles.setdefault(src, presses)
    result = 1
    for c in cycles.values():
        result = result * c // gcd(result, c)
    print("Czesc 2:", result)


main()
