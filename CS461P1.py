# CS461P1 by Alex Arbuckle #


# Import <
from random import shuffle

# >


# Main <
if (__name__ == '__main__'):

    # while (not q, Q) <
    while (input('[C]ontinue\n[Q]uit\n\nInput : ') not in ['q', 'Q']):

        # Declaration <
        suit, sim = ('C', 'H', 'S', 'D'), 500
        deck = [f'{j}{i}' for j in range(1, 14) for i in suit]
        total = {k : 0 for k in ['Pass', 'Part', 'Game', 'Small Slam', 'Grand Slam']}
        cardDict, distDict = {'1' : 4, '11' : 1, '12' : 3, '13' : 3}, {2 : 1, 1 : 2, 0 : 5}

        # >

        # Evaluate <
        shuffle(deck)
        a = [deck[i] for i in range(13)]
        [deck.pop(i) for i in range(13)]
        for i in range(sim):

            shuffle(deck)
            b, score = [deck[i] for i in range(13, 26)], 0
            for h in [a, b]:

                # Distribution Count <
                ab = [i[-1] for i in h]
                score += sum([distDict[ab.count(s)] for s in suit if (ab.count(s) in distDict.keys())])

                # >

                # High-Card Count <
                ab = [i[0] + i[1] for i in h]
                score += sum([cardDict[c] for c in ab if (c in cardDict.keys())])

                # >

                print(score)
                input('; ')

            # Update Total <
            if (31 < score < 36): total['Small Slam'] += score
            if (score > 35): total['Grand Slam'] += score
            if (19 < score < 26): total['Part'] += score
            if (25 < score < 32): total['Game'] += score
            if (score < 20): total['Pass'] += score

            # >
 
        # >

        # Output <
        strVariable = '\n'.join([f'{k} : {v / sim}%' for k, v in total.items()])
        print(f'\nResult :\n\n{strVariable}\n')

        # >

    # >    

# >
