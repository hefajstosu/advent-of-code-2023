import sys


def hash_str(s):
    v = 0
    for ch in s:
        v = (v + ord(ch)) * 17 % 256
    return v


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        steps = f.read().replace("\n", "").strip().split(",")

    part1 = sum(hash_str(s) for s in steps)

    # pudelka z soczewkami
    boxes = [dict() for _ in range(256)]
    for s in steps:
        if s.endswith("-"):
            label = s[:-1]
            boxes[hash_str(label)].pop(label, None)
        else:
            label, focal = s.split("=")
            boxes[hash_str(label)][label] = int(focal)

    part2 = 0
    for b, box in enumerate(boxes):
        for slot, focal in enumerate(box.values()):
            part2 += (b + 1) * (slot + 1) * focal

    print("Czesc 1:", part1)
    print("Czesc 2:", part2)


if __name__ == "__main__":
    main()
