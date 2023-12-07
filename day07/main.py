import sys
from collections import Counter


def hand_type(hand, joker):
    counts = Counter(hand)
    jokers = 0
    if joker:
        jokers = counts.pop("J", 0)
    shape = sorted(counts.values(), reverse=True) or [0]
    # jokery doklejamy
    shape[0] += jokers
    return shape


def key(hand, joker):
    order = "J23456789TQKA" if joker else "23456789TJQKA"
    return (hand_type(hand, joker), [order.index(c) for c in hand])


def winnings(hands, joker):
    ranked = sorted(hands, key=lambda hb: key(hb[0], joker))
    return sum(i * bid for i, (_, bid) in enumerate(ranked, 1))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    hands = []
    with open(path) as f:
        for line in f:
            if line.strip():
                h, b = line.split()
                hands.append((h, int(b)))
    print("Czesc 1:", winnings(hands, False))
    print("Czesc 2:", winnings(hands, True))


main()
