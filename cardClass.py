class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    VALS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, vals=0):
        self.suit = suit
        self.vals = vals

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.VALS[self.vals],
                                   Card.SUITS[self.suit])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

            
for i in range (6):
    pygame.draw.polygon(win, BLACK, [[x[i]-40, y[i]+55], [x[i]+40, y[i]+55], [x[i], y[i]]])
    pygame.draw.ellipse(win,BLACK,[x[i]-50,y[i]+45,60,60])
    pygame.draw.ellipse(win,BLACK,[x[i]-10,y[i]+45,60,60])
    pygame.draw.polygon(win, BLACK, [[x[i]-25, y[i]+130], [x[i]+25, y[i]+130], [x[i], y[i]+90]])
