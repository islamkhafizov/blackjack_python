# importing random library to get a random number for the card
import random


# main function to handle the program
def main():
    print("Starting game...")

    # keep playing rounds again and again as long as player wants
    user_choice = 'y'
    while user_choice == 'y':
        # run a round of the game
        play_round()

        # after the round ask the player if they want to play again
        user_choice = input("Would you like to play again(y/n)?").lower()

        # make user enters yes or no
        while user_choice != 'y' and user_choice != 'n':
            print("Invalid input!")
            user_choice = input("Would you like to play again(y/n)?").lower()

    print("Thank you for playing!\nBye...")


# function to play a round of the gmae
def play_round():
    # get the cards already shuffled
    cards = get_cards()

    # nested lists to hold the cards of each player
    players_cards = [
        [], []
    ]

    # list to store the score of both the player
    scores = [0, 0]

    # for each player
    for p in range(len(players_cards)):
        # run two times
        for x in range(2):
            # give a random card to a player
            pick_a_card(players_cards[p], cards)

        # calculate the player scores from the cards given
        scores[p] = get_player_score(players_cards[p])

    # variable to know which players turn it is
    playing_player = 0

    player_stands = [False, False]

    # the round will continue til this boolean is true
    round_playing = True
    while round_playing:
        if not player_stands[playing_player]:
            # call the function to print the cards of the player and the score
            print_players(players_cards, scores)

            # ask the player if they want to hit or stand
            player_choice = input(f"Player{playing_player + 1}, what is your choice - Hit(H) or Stand(S)?: ").lower()

            # make sure player enters either h or s
            while player_choice != 'h' and player_choice != 's':
                print("Invalid entry!")
                player_choice = input(f"Player{playing_player + 1}, what is your choice - Hit(H) or Stand(S)?: ").lower()

            # if the player wants to hit
            if player_choice == 'h':
                # pick a card from he decks
                pick_a_card(players_cards[playing_player], cards)

                # update the score of the player
                scores[playing_player] = get_player_score(players_cards[playing_player])
            else:
                player_stands[playing_player] = True

        # pass the turn to the next player
        playing_player = 1 - playing_player

        # check if anyone of both players had crossed 21
        if scores[0] > 21 or scores[1] > 21 or (player_stands[0] and player_stands[1]):
            # show the players' cards and print the scores for both players
            print_players(players_cards, scores)

            # if both player stand
            if player_stands[0] and player_stands[1]:

                # if both player have the same amount its a tie
                if scores[0] == scores[1]:
                    print("It's a draw!")

                # check for higher score player
                elif scores[0] > scores[1]:
                    print("Player 1 Wins!")
                else:
                    print("Player 2 Wins!")

            # if the first player exceeded 21
            elif scores[0] > 21:
                # player 2 wins
                print("Player 2 Wins!")

            # if the second player exceeded 21
            elif scores[1] > 21:
                # player 1 wins
                print("Player 1 Wins!")

            # set the boolean false to stop the loop fom running further
            round_playing = False


# function to print the cards and the score of the player
def print_players(players_cards, scores):
    # for each set of player cards
    for x in range(len(players_cards)):
        # print the score and the cards for the player
        print(f"Player{x + 1}: {' + '.join(players_cards[x])} = {scores[x]}")


# function to get the score of a player from cards
def get_player_score(player_cards):
    # list to hold the cards with value of 10
    values_of_10 = ["J", "Q", "K", "10"]

    # to keep track if blackjack condition happens
    is_blackjack = False
    score = 0

    # if we are at the starting round with player having only two cards
    if len(player_cards) == 2:
        # remove the eck symbol
        card_1 = player_cards[0][:-1]
        card_2 = player_cards[1][:-1]

        # check if in one hand we have an ace and in the other we have cards with a value of 10
        if (card_1 == "A" and card_2 in values_of_10) or (card_2 == "A" and card_1 in values_of_10):
            # if the condition is true then we have a blackjack situation
            is_blackjack = True

    # if we dont have a blackjack condition
    if not is_blackjack:
        # for each card in the players card
        for card in player_cards:
            # remove the deck symbol
            card = card[:-1]

            # treat ace as 1
            if card == "A":
                score += 1
            # treat the others which have a value of 10
            elif card in values_of_10:
                score += 10

            # and the others as the value they have
            else:
                score += int(card)

    # if there is a blackjack
    else:
        # set score to 21
        score = 21

    # return the score
    return score


# function to give a random card to the player
def pick_a_card(player, cards):
    # get a random card from the deck
    card_index = random.randint(0, len(cards) - 1)
    card = cards[card_index]

    # remove the card from the deck
    del cards[card_index]

    # give the card to the player
    player.append(card)


# function all 52 cards already shuffled
def get_cards():
    cards = []
    decks = ["H", "C", "S", "D"]

    # for each deck we create cards
    for deck in decks:
        for x in range(1, 14):
            # if the card is 1 treat it as ACE
            if x == 1:
                cards.append(f"A{deck}")

            # if card is 11 treat it as Joker
            elif x == 11:
                cards.append(f"J{deck}")

            # if card is 12 treat it as Queen
            elif x == 12:
                cards.append(f"Q{deck}")

            # if card is 13th tret it as King
            elif x == 13:
                cards.append(f"K{deck}")

            # else the card numerical value is the same as the loop variable
            else:
                cards.append(f"{x}{deck}")

    # call the function to shuffle the cards
    fisher_yates_shuffle(cards)

    # return the 52 shuffled cards
    return cards


# function to shuffle cards using fisher yates shuffle
def fisher_yates_shuffle(cards):
    n = len(cards)
    # loop though the index in reverse
    for i in range(n - 1, 0, -1):
        # getting a random integer in range
        j = random.randint(0, i + 1)
        # swap
        cards[i], cards[j] = cards[j], cards[i]


# call the main function that handles the program
main()
