#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d = CardDeck("Suzie")
print(d)
print(d.get_dealer())

print(d.dealer)

d.dealer = 'Bob'

print(d.dealer)

try:
    d.dealer = 12.34
except TypeError as err:
    print(err)
else:
    print(d.dealer)

d.shuffle()
print(d.cards)
print()

hand = []
for i in range(5):
    hand.append(d.draw())

print("Hand:", hand)

print(str(d))
print(len(d.cards))

print(len(d))

d2 = CardDeck("Mary")

d3 = d + d2

print(d3)

j1 = JokerDeck('Albert')
j1.shuffle()

d4 = d + j1

print(d4)

print(j1.cards)

j1.barf()

print(JokerDeck.mro())
