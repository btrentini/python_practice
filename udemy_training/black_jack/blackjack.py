"""
Blackjack main class created by Bruno Trentini

- Need to implement mechanism to deal with further bets
"""
import deck as dk
import player as pl
import hand as hd

def check_bets():
    '''do nothing here'''

    if bet >= balance:
        print("This is ok")

    else:
        print("This is NOT ok")



def play_again():

    while True:
        try:
            pl_again = input(
                "\n\t> Pres enter to play again or N to exit: ").strip().upper()
        except:
            print("\n\t[!] Wrong input. Please type [N/any]")
            continue
        else:
            break

    if pl_again != "N":
        return True
    else:
        print(f"\n\t > Your final balance {PLAYER.balance} ==\n")
        return False

def check_sum_dealer():

    temp_sum = 0

    for idx, card in enumerate(DEALER.hand.cards):

        if len(card) == 3:
            temp_sum += MYDECK.card_values[card[0:2]]
        else:
            temp_sum += MYDECK.card_values[card[0]]

    return DEALER.cards_sum(temp_sum)

def check_sum_player():

    temp_sum = 0

    for idx, card in enumerate(PLAYER.hand.cards):

        if len(card) == 3:
            temp_sum += MYDECK.card_values[card[0:2]]
        else:
            temp_sum += MYDECK.card_values[card[0]]

    return PLAYER.cards_sum(temp_sum)


def check_play(player):
    '''Checks game progress and actions taken'''
    print(player.player_type)

    if player.player_type.upper() != "DEALER":
        result = check_sum_player()
    else:
        result = check_sum_dealer()

    if result == "BJ":
        print("\n=====================================")
        print(f"\t> {player.player_type.upper()} BLACKJACK!!")
        print("=====================================")
        return False
    elif result == "21":
        print("\n=====================================")
        print(f"\t> {player.player_type.upper()} Vingt-et-un")
        print("=====================================")
        return False
    elif result == "BURST":
        print("\n=====================================")
        print(f"\t> {player.player_type.upper()} BURST")
        print("=====================================")
        return False
    else:
        return True


def actions():
    '''Allow user to choose an action. Eg: Hit or Surrender'''

    actions = ["Hit", "Stand", "Surrender"]

    print("\n\tWhat do you want to do?")

    for idx, act in enumerate(actions):
        print(f"\t{idx+1} : {act}")

    while True:
        try:
            action_chosen = int(input("\n\tAction > "))
        except ValueError:
            print(
                f"\t[!] Choose a valid action using numbers 1 to {len(actions)}")
            continue
        else:
            if action_chosen < 1 or action_chosen > len(actions):
                print(
                    f"\t[!] Choose a valid action using numbers 1 to {len(actions)}")
                continue
            else:
                break

    return actions[action_chosen - 1]


def bet():
    '''Gets an input regarding the player's bet'''

    print(
        f"\n\tP1  > How much you want to bet? \t | Your balance: {PLAYER.balance}")

    while True:
        try:
            bet = int(input("\n\tBet > "))
        except ValueError:
            print(
                f"\t[!] Choose a valid action using whole numbers")
            continue
        else:
            if bet < 1 or bet > PLAYER.balance:
                print(
                    f"\t[!] Enter a valid number. Your balance is {PLAYER.balance}")
                continue
            else:
                break

    PLAYER.update_balance(-bet)

    print(f"\n\tP1     > {PLAYER.print_hand()}")
    print(f"\tDealer > {DEALER.print_hand()}")


def blackjack():
    '''Starts the game and contains function calls'''
    bet()

    while True:

        action = actions().upper()

        if action == "HIT":
            PLAYER.hand.hit(PACK)
            if not check_play(PLAYER):
                break
            else:
                continue

        if action == "SURRENDER":
            break

        if action == "STAND":
            DEALER.hand.set_initial_count(PLAYER.hand.initial_count)

            while DEALER.sum_cards < 17:
                print("_________________")
                print(f"DEALER: {DEALER.sum_cards}")
                print(f"HUMAN: {PLAYER.sum_cards}")
                print("_________________")

                if DEALER.sum_cards > PLAYER.sum_cards:
                    print("DEALER WINS")
                    break
                else:
                    DEALER.hand.hit(PACK)
                    if not check_play(DEALER):
                        break
                    else:
                        continue
            else:
                break


if __name__ == "__main__":

    print("\n=====================================")
    print("\tBLACKJACK")
    print("=====================================")

    # Initialises the Deck
    MYDECK = dk.Deck()
    PACK = MYDECK.shuffle()

    # Initialises player and dealer
    PLAYER = pl.Player(player_type="user", balance=500,
                       hand=hd.Hand(PACK[0:2]))
    DEALER = pl.Player(player_type="dealer", balance=5000,
                       hand=hd.Hand(PACK[2:4]))

    blackjack()
