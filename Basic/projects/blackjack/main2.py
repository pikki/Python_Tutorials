"""
Name : Himalaya Kilaru
Email : himalay.kilaru@gmail.com
Date :30/10/2021
Project : BlackJack
"""

###################################### Black Project Starts Here ###################################

# Here we start

## Importing Dependencies
import random

# Logo
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


# Create a function called as deal_card() that uses the list called as cards to return a random card.
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Create a function called as calculate_score() that takes the list of cards and returns the score.
def calculate_score(cards):
    """takes the list of cards and returns the score"""
    # We will check for a blackjack and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # We will check for an 11. If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Create a function called compare() and pass in the user_score and computer_score. If the computer and user both
# have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a
# blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over
# 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    # Bug Fix
    if user_score > 21 and computer_score > 21:
        print("You went over. You lose.")
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        print("Opponent Went over. You win.")
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You lose"


def play_game():
    print(logo)
    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"You cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card()))
        computer_score = calculate_score(computer_cards)
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
