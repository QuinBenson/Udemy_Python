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

    def __init__(self, internal_name, player_type, player_number, hit_score_max):
        self.internal_name = internal_name
        self.player_type = player_type
        self.player_number = player_number
        self.hit_score = hit_score_max
        self.current_score = 0
        self.card_hand = []


def show_hand(participant, show_dealer_total):

    hold_hand = participant.card_hand[:]

    if participant.player_type == "D":
        display_name = "Dealer"

        if not show_dealer_total:
            del hold_hand[0]
            hold_hand.insert(0, "-")
            display_string = f"{display_name:>9}: {hold_hand}"
        else:
            display_string = f"{display_name:>9}: {hold_hand} {participant.current_score}"
    else:
        display_name = f"Player {participant.player_number:02d}"
        display_string = f"{display_name:>9}: {hold_hand} {participant.current_score}"

    print(f"{display_string}")


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
player_turn_end = False
while not finish:
    play = input("Play Blackjack? ").lower()
    if play == "y":
        player_turn_end = False
    else:
        finish = True

    while not finish and not player_turn_end:
        # Setup/reset
        player_count = 0

        # store dealer at index zero in player list
        player_list = [Participant("Dealer", "D", 0, 17)]

        # add players (current range: one player only)
        for i in range(1, 2):
            player_count += 1
            player_list.append(Participant(player_name_str(player_count), "P", player_count, 21))

            # Deal 2 cards each
            for player_delt in player_list:
                for j in range(0, 2):
                    player_delt.card_hand.append(deal_a_card())
                    player_delt.current_score = sum(player_delt.card_hand)
            # test print area
            for n in range(len(player_list)):
                show_hand(player_list[n], False)
            # Loop through all players
            for player_turn in range(1, len(player_list)):
                player_turn_end = False
                while not player_turn_end:
                    turn_pass = input(
                        f"Player {player_list[player_turn].player_number:02d} "
                        f"Type 'y' to get another card, type 'n' to pass ").lower()
                    if turn_pass == "n":
                        player_turn_end = True
                    else:
                        # TODO functionalise the card handling for players and the dealer


                        player_list[player_turn].card_hand.append(deal_a_card())
                        # DEBUG CODE
                        player_list[player_turn].card_hand[-1] = 11

                        player_list[player_turn].current_score = sum(player_list[player_turn].card_hand)



                        while 11 in player_list[player_turn].card_hand and player_list[player_turn].current_score >= 21:
                            ace_index = player_list[player_turn].card_hand.index(11)

                            player_list[player_turn].card_hand[ace_index] = 2
                            player_list[player_turn].current_score = sum(player_list[player_turn].card_hand)



                    show_hand(player_list[player_turn], False)
                    if player_list[player_turn].current_score >= 21:
                        player_turn_end = True

            dealer_turn_end = False
            while not dealer_turn_end:
                if player_list[0].current_score >= player_list[0].hit_score:
                    dealer_turn_end = True
                else:
                    player_list[0].card_hand.append(deal_a_card())
                    player_list[0].current_score = sum(player_list[0].card_hand)

            show_hand(player_list[0], True)
            show_hand(player_list[player_turn], True)

        # TODO Thank you and goodnight

        # player_list[1].current_score = 12
        # player_list[0].current_score = 17
