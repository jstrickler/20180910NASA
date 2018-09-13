#!/usr/bin/env python
import random

class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = [
            (rank, suit)
            for suit in self.SUITS
                for rank in self.RANKS
        ]

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    # getter method (AKA accessor method)
    def get_dealer(self):
        return self._dealer

    def set_dealer(self, dealer):
        self._dealer = dealer

    # getter property
    # @property
    def dealer(self):
        return self._dealer.upper()

    dealer = property(dealer)

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            bad_type = type(dealer).__name__
            raise TypeError(f"Dealer must be a string, not a {bad_type}")

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_name = type(self).__name__
        return f"{my_name}({len(self)})"

    def __add__(self, other):
        tmp = CardDeck(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp
