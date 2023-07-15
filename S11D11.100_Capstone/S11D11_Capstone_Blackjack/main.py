# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
import random
import prettytable as pt

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

HandTable = pt.PrettyTable(border=False, header=False)

class Participant:

    def __init__(self, internal_name, player_type, player_number, hit_score_max):
        self.internal_name = internal_name
        self.player_type = player_type
        self.player_number = player_number
        self.hit_score = hit_score_max
        self.current_score = 0
        self.card_hand = []
        self.play_status = ""
        self.outcome = ""

    def deal_and_adjust(self):
        self.card_hand.append(deal_a_card())

        self.current_score = sum(self.card_hand)

        while 11 in self.card_hand and self.current_score >= 21:
            ace_index = self.card_hand.index(11)

            self.card_hand[ace_index] = 1
            self.current_score = sum(self.card_hand)

        if self.current_score > 21:
            self.play_status = "Bust"


    def show_hand(self, show_dealer_total):
        """displays the hand of cards being played by the invoked participant.
        NB show_dealer_total is only applicable to the Dealer participant and otherwise ignored"""
        display_list=[]
        hold_hand = self.card_hand[:]
        hold_score = str(self.current_score)

        if self.player_type == "D":
            display_name = "Dealer"

            if not show_dealer_total:
                del hold_hand[0]
                hold_hand.insert(0, "—")

                hold_score = ""
            else:
                pass
        else:
            display_name = f"Player {self.player_number:02d}"
        str1 = ' '.join(str(e) for e in hold_hand)
        str1 = "[" + str1 + "]"

        display_list.extend([display_name, str1, hold_score,self.outcome])
        return display_list


def player_name_str(player_number):
    """format the player name label/object name"""
    return f"Player_{player_number:02d}"


def deal_a_card():
    global cards
    return cards[random.randint(0, 12)]


finish_game = False
player_turn_end = False
while not finish_game:
    play_game = input("Play Blackjack? ").lower()
    if play_game == "y":
        player_turn_end = False
    else:
        finish_game = True

    while not finish_game and not player_turn_end:
        # Setup/reset
        player_count = 0

        # Initialise dealer at index zero in player list
        player_list = [Participant("Dealer", "D", 0, 17)]

        # Initialise players (current range: one player only)
        for i in range(1, 2):
            player_count += 1
            player_list.append(Participant(player_name_str(player_count), "P", player_count, 21))

            # Deal 2 cards each
            for player_being_delt in player_list:
                for j in range(0, 2):
                    player_being_delt.deal_and_adjust()

            # Show hands of cards with dealer's second card hidden
            for all_the_participants in player_list:
                HandTable.add_row( all_the_participants.show_hand(False))

            #HandTable.left_padding_width =  #=max(player_list, key=len)
            # HandTable._max_width = {"Field 1": 6, "Field 2": 25}
            #HandTable._align = {"Field 1": "r", "Field 2": "c", "Field 3": "r", "Field 4": "c"}
            # not accepted use?
            HandTable.padding_width = 2
            HandTable.align['Field 1'] = "r"
            HandTable.align['Field 2'] = "c"
            HandTable.align['Field 3'] = "r"
            HandTable.align['Field 4'] = "c"

            print(HandTable)
            HandTable.clear()
           # HandTable=[] this blows the prettytable class

            # Loop through all players, excluding dealer
            for current_players_turn in player_list[1:]:
                player_turn_end = False
                while not player_turn_end:
                    player_passes = input(
                        f"Player {current_players_turn.player_number:02d} "
                        f"Type 'y' to get another card, type 'n' to pass ").lower()
                    if player_passes == "n":
                        player_turn_end = True
                        current_players_turn.play_status = "Hold"
                    else:
                        current_players_turn.deal_and_adjust()

                        HandTable.add_row(player_list[0].show_hand(False))
                        HandTable.add_row(current_players_turn.show_hand(False))

                        #HandTable.align['Field 1'] = "r"
                        HandTable.padding_width = 2
                        HandTable.align['Field 1'] = "r"
                        HandTable.align['Field 2'] = "c"
                        HandTable.align['Field 3'] = "r"
                        HandTable.align['Field 4'] = "c"
                        print(HandTable)
                        HandTable.clear()

                    if current_players_turn.current_score >= 21:
                        player_turn_end = True

            dealer_turn_end = False

            while not dealer_turn_end:
                if player_list[0].current_score >= player_list[0].hit_score:
                    dealer_turn_end = True
                else:
                    player_list[0].deal_and_adjust()
            # Show hands of cards with dealer's second card shown

            for participant in player_list[1:]:
                #  work out winners

                if participant.play_status == "Bust":
                    participant.outcome = "Lose"
                    player_list[0].outcome = "Win"
                elif player_list[0].play_status == "Bust":
                    participant.outcome = "Win"
                    player_list[0].outcome = "Lose"
                elif player_list[0].current_score > participant.current_score:
                    participant.outcome = "Lose"
                    player_list[0].outcome = "Win"
                elif player_list[0].current_score == participant.current_score:
                    participant.outcome = "Draw"
                    player_list[0].outcome = "Draw"
                else:
                    participant.outcome = "Win"
                    player_list[0].outcome = "Lose"

            for participant in player_list:
                HandTable.add_row(participant.show_hand(True))

            HandTable.padding_width = 2
            HandTable.align['Field 1'] = "r"
            HandTable.align['Field 2'] = "c"
            HandTable.align['Field 3'] = "r"
            HandTable.align['Field 4'] = "c"

            print(HandTable)
            HandTable.clear()
