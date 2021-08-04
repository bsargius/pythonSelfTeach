class Card:
    def __init__(self, suite_input, rank_input):
        self.suite_input = suite_input
        self.rank_input = rank_input


class Deck:
    def __init__(self, card_input):
        self.card_input = card_input


suite = ["Hearts", "Diamonds", "Clubs", "Spades"]
rank = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


