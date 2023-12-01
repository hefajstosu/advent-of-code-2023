import sys

WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def digits(line, words):
    # wyciagamy cyfry
    out = []
    for i, c in enumerate(line):
        if c.isdigit():
            out.append(int(c))
        elif words:
            for v, w in enumerate(WORDS, 1):
                if line.startswith(w, i):
                    out.append(v)
                    break
    return out


def value(line, words):
    d = digits(line, words)
    return d[0] * 10 + d[-1] if d else 0


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    print("Czesc 1:", sum(value(l, False) for l in lines))
    print("Czesc 2:", sum(value(l, True) for l in lines))


main()
