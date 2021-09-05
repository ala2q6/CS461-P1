# CS461P1 by Alex Arbuckle #


# Import <
from random import shuffle

# >


# Main <
if (__name__ == '__main__'):

    # while (not q, Q) <
    while (input('[C]ontinue\n[Q]uit\n\nInput : ') not in ['q', 'Q']):

        # Declaration <
        score, suit = [0, 0, 0, 0, 0], ('C', 'H', 'S', 'D')
        deck = [f'{j}{i}' for j in range(1, 14) for i in suit]
        cardCount, distCount = {'1' : 4, '11' : 1, '12' : 3, '13' : 3}, {2 : 1, 1 : 2, 0 : 5}

        # >

        # Evaluate <
        shuffle(deck)
        a = [deck[i] for i in range(13)]
        [deck.pop(i) for i in range(13)]
        for i in range(500):

            shuffle(deck)
            b, count = [deck[i] for i in range(13, 26)], 0
            for d in [a, b]:

                # Distribution Count <
                c = [i[-1] for i in d]

                # >

                # High-Card Count <
                c = [i[0] + i[1] for i in d]

                # >

            #count += sum([distCount[(a + b).count(s)] for s in suit if ((a + b).count(s) in distCount.keys())])

        # >

    # >

# >
