#!/usr/bin/env python

from carddeck import CardDeck

class Wombat():
    def barf(self):
        print("barfing....")

class JokerDeck(CardDeck, Wombat):

    def _create_deck(self):
        super()._create_deck()
        self._cards.append(('Joker',1))
        self._cards.append(('Joker',2))
