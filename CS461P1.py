# CS461P1 by Alex Arbuckle #


# Import <
from random import shuffle

# >


# Main <
if (__name__ == '__main__'):

    # while (not q, Q) <
    while (input('[Enter]\tto continue\n[Q]\t\tto quit\n\nInput : ') not in ['q', 'Q']):

        # Declaration <
        value = {'1' : 4, '11' : 1, '12' : 3, '13' : 3}
        suit, score = ('C', 'H', 'S', 'D'), [0, 0, 0, 0, 0]
        deck = [f'{j}{i}' for j in range(1, 14) for i in suit]

        # >

        shuffle(deck)
        handA = [deck[i] for i in range(13)]
        handB = [deck[i] for i in range(13, )]
        [deck.pop(i) for i in range(13)]

    # >

# >

# Example <
# ks 8s 6s 5s kh 10h 7h 5h 3h 7d jc 8c 6c
# 3         + 3                + 1
#                             + 2

# >
