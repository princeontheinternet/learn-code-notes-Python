#

import random

# Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # We used tuples as it is fixed and we don't want to add or remove.
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """
    This class will tell you about your card.
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """
    This class will hold and shuffle all the cards
    """

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    """
    This class will have Player's name and card that he has after removing and adding.
    Rem: We add card at the bottom and remove from the top.
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        if type(new_cards) == type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)
        # using extend because if we have multiple cards then we can append it one by one.

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} card/s."


# ###################### START OF GAME LOGIC ###################

# 1. ****** GAME SETUP *****
player_one = Player("One")
player_two = Player("Two")

# 2. **** Instantiating Deck class and then shuffling the cards. ****
new_deck = Deck()
new_deck.shuffle()
# for card in new_deck.all_cards:   # check the shuffle cards
#     print(card)


# 3. **** Distributing the cards ****
for x in range(26):
    player_one.add_cards(new_deck.deal_one())  # deal one will pop a card from shuffled cards
    player_two.add_cards(new_deck.deal_one())

# Player 1 cards
# for i,j in enumerate(player_one.all_cards):
#     print(i, j)

# 4. Play the Game

game_on = True
round = 0

while game_on:

    round += 1
    print(f"Round: {round}")

    # 1. **** Check if player out of card ****
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    # Otherwise, the game is still on!

    # 2. **** Start a new round and reset current cards "on the table" ****
    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]

    at_war = True

    while at_war:

        # Check for 3 conditions
        # 1. player1 card value > player2 card value, if yes than add card to player 1
        # 2. vice versa of 1
        # 3. both values equal then at war

        # 1.
        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        # 2.
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        # 3.
        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break

            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
