import sys


def parse(text):
    wf_text, parts_text = text.strip().split("\n\n")
    workflows = {}
    for line in wf_text.splitlines():
        name, rest = line.strip().rstrip("}").split("{")
        rules = []
        for rule in rest.split(","):
            if ":" in rule:
                cond, target = rule.split(":")
                rules.append((cond[0], cond[1], int(cond[2:]), target))
            else:
                # domyslna regula
                rules.append((None, None, None, rule))
        workflows[name] = rules
    parts = []
    for line in parts_text.splitlines():
        part = {}
        for kv in line.strip().strip("{}").split(","):
            k, v = kv.split("=")
            part[k] = int(v)
        parts.append(part)
    return workflows, parts


def accepted(workflows, part):
    name = "in"
    while name not in ("A", "R"):
        for key, op, val, target in workflows[name]:
            if key is None or (op == "<" and part[key] < val) or (op == ">" and part[key] > val):
                name = target
                break
    return name == "A"


def count(workflows, name, ranges):
    # przedzialy kategorii
    if name == "R":
        return 0
    if name == "A":
        total = 1
        for lo, hi in ranges.values():
            total *= hi - lo + 1
        return total
    total = 0
    ranges = dict(ranges)
    for key, op, val, target in workflows[name]:
        if key is None:
            total += count(workflows, target, ranges)
            break
        lo, hi = ranges[key]
        # dzielimy przedzial
        if op == "<":
            yes, no = (lo, min(hi, val - 1)), (max(lo, val), hi)
        else:
            yes, no = (max(lo, val + 1), hi), (lo, min(hi, val))
        if yes[0] <= yes[1]:
            sub = dict(ranges)
            sub[key] = yes
            total += count(workflows, target, sub)
        if no[0] > no[1]:
            break
        ranges[key] = no
    return total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        workflows, parts = parse(f.read())
    print("Czesc 1:", sum(sum(p.values()) for p in parts if accepted(workflows, p)))
    print("Czesc 2:", count(workflows, "in", {k: (1, 4000) for k in "xmas"}))


main()
