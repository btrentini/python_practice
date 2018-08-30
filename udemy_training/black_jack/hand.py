"""
Normal User Type of Player
"""


class Hand:
    '''pass'''

    def __init__(self, player_cards):
        '''initialises the Hand'''
        self.cards = player_cards
        self.initial_count = 4

    def show_cards(self):
        '''shows the cards of a hand'''

        return self.cards

    def set_initial_count(self, initial_count):
        '''helps pessing the last used card of the pack'''

        self.initial_count = initial_count

    def assign_pack(self, player_cards):
        '''Assign a new pakc'''

        self.cards = player_cards
        self.initial_count = 4

    def hit(self, pack):
        '''When player presses hit, show another card'''

        self.pack = pack
        self.newcard = pack[self.initial_count]
        self.initial_count += 1

        self.cards.append(self.newcard)

        return self.cards
