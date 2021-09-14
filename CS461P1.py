# CS461P1 by Alex Arbuckle #


# Import <
from random import shuffle

# >


# Main <
if (__name__ == '__main__'):

    # while not q or Q <
    print('Monte Carlo Simulation\n')
    while (input('[C]ontinue\n[Q]uit\n\nInput: ') not in ['q', 'Q']):

        # Declaration <
        suit, sim = ('C', 'H', 'S', 'D'), 1000
        deck = [f'{j}{i}' for j in range(1, 14) for i in suit]
        total = {k : 0 for k in ['Pass', 'Part', 'Game', 'Small', 'Grand']}
        highDict, distDict = {'1' : 4, '11' : 1, '12' : 2, '13' : 3}, {2 : 1, 1 : 2, 0 : 5}
        highFunc = lambda hand : sum([highDict[card] for card in hand if (card in highDict.keys())])
        distFunc = lambda h : sum([distDict[h.count(s)] for s in suit if (h.count(s) in distDict.keys())])

        # >

        # Evaluate <
        shuffle(deck)
        a = [deck[i] for i in range(13)]
        [deck.pop(i) for i in range(13)]
        ac = distFunc([c[-1] for c in a]) + highFunc([c[:-1] for c in a])
        for i in range(sim):

            shuffle(deck)
            b, score = [deck[c] for c in range(13, 26)], 0
            bc = distFunc([c[-1] for c in b]) + highFunc([c[:-1] for c in b])

            # Update <
            if (31 < (ac + bc) < 36): total['Small'] += 1
            if (25 < (ac + bc) < 32): total['Game'] += 1
            if (19 < (ac + bc) < 26): total['Part'] += 1
            if ((ac + bc) > 35): total['Grand'] += 1
            if ((ac + bc) < 20): total['Pass'] += 1

            # >

        # >

        # Output <
        out = '\n'.join([f'{k}\t{round((v / sim) * 100, 2)}%' for k, v in total.items()])
        print('\n\nHand: {}\nCount: {}\nResult:\n\n{}\n\n'.format(a, ac, out))

        # >

    # >

# >
