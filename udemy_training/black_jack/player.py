"""
Defines players
"""


class Player:
    '''class player'''

    def __init__(self, player_type, balance, hand):
        '''initialises a player'''

        self.player_type = player_type
        self.balance = balance
        self.hand = hand
        self.sum_cards = 0
        self.result = ""

    def update_balance(self, balance):
        '''updates player balance'''
        self.balance += balance

    def check_balance(self, bet):

        if self.balance >= bet:
            print("This is ok")
        else:
            print("This is NOT ok")

    def print_hand(self):
        '''prints the player hand'''

        if self.player_type.upper() == "DEALER":
            return self.hand.cards[0]
        else:
            return self.hand.cards

    def cards_sum(self, sum_cards):
        '''shows the sum of a hand'''

        self.sum_cards = sum_cards

        print("__________________________")
        print(f"{self.hand.cards} = {self.sum_cards}")
        print("__________________________")


        if len(self.hand.cards) == 2 and self.sum_cards == 21:
            self.result = "BJ"
            self.sum_cards = 0
        if self.sum_cards == 21:
            self.result = "21"
            self.sum_cards = 0
        elif self.sum_cards > 21:
            self.result = "BURST"
            self.sum_cards = 0
        else:
            pass

        return self.result
