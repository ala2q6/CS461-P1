suit, sim = ('C', 'H', 'S', 'D'), 500
deck = [f'{j}{i}' for j in range(1, 14) for i in suit]


ab = [c[:-1] for c in deck]
ac = [c[0] + c[1] for c in deck]


for i in range(len(deck)):

    print(f'{deck[i]}\t\t{ab[i]}')
