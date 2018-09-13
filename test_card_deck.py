#!/usr/bin/env python
import sys
from unittest import TestCase, main, skipUnless
from carddeck import CardDeck

TEST_USER = "test user"

class TestCardDeck(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.deck = CardDeck(TEST_USER)

    def test_card_deck_has_52_cards(self):
        self.assertEqual(52, len(self.deck), "New deck did not have 52 cards")

    # @skipUnless(sys.platform == 'win32', 'only implemented on Windows')
    def test_drawing_one_card_reduces_length_by_one(self):
        self.deck.draw()
        self.assertEqual(51, len(self.deck), "Drawing one card did not reduce length by one")

    def tearDown(self):
        pass



if __name__ == '__main__':
    main(verbosity=11) # test runner


