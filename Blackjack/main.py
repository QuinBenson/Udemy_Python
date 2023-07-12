# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
import random

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Participant:

    def __init__(self, name, hit_score_max):
        self.name = name
        self.hit_score = hit_score_max
        self.current_score = 0
        self.card_hand = []


def show_hand(participant):
    print(f"{participant.name} {participant.card_hand} {participant.current_score}")


def player_name_str(player_number):
    """format the player name label/object name"""
    return f"Player_{player_number:02d}"


def deal_a_card():
    global cards
    return cards[random.randint(0, 12)]


# TODO Start of main()

# TODO 01 Play a game? Prompt
# TODO 01.01 init players
finish = False
turn_end = False
while not finish:
    play = input("Play? ").lower()
    if play == "y":
        turn_end = False
    else:
        finish = True

    while not finish and not turn_end:
        # Setup
        player_count = 0

        # store dealer at index zero in player list
        player_list = [Participant("Dealer", 17)]

        # add players (current range: one player only)
        for i in range(1, 2):
            player_count += 1
            player_list.append(Participant(player_name_str(player_count), 0))

        # Deal 2 cards each
        for player_delt in player_list:
            for i in range(0, 2):
                player_delt.card_hand.append(deal_a_card())
                player_delt.current_score=sum(player_delt.card_hand)
        # test print area
        for n in range(len(player_list)):
            show_hand(player_list[n])

        for player_turn in range( 1, len(player_list)):
            while not turn_end:
                turn_pass=input("Type 'y' to get another card, type 'n' to pass ").lower()
                if turn_pass == "n":
                    player_list[player_turn].card_hand.append(deal_a_card())
                    player_list[player_turn].current_score = sum(player_list[player_turn].card_hand)
                    show_hand(player_list[player_turn])
                    if player_list[player_turn].current_score >= 21:
                        turn_end = True
                else:
                    turn_end = True


        # TODO Loop: Remainder of play: Deal Cards while game is in question

        # TODO Thank you and goodnight

        # player_list[1].current_score = 12
        # player_list[0].current_score = 17
