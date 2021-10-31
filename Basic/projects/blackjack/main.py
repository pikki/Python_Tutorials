import random


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
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'K', 'Q', 'J']
game = True
player_score = 0
comp_score = 0


def game_start():
### is there a better way and why didnt I have to declare cards as global but still able to acess it ?
    global player_score
    global comp_score
    global game
    del cards[-1]
    player_cards = random.sample(cards, 2)
    comp_cards = random.sample(cards, 2)
    black_jack = ['A','10','K','Q','L']
    print_cards('Your',player_cards,0)
    print_cards('Computer', comp_cards, 0)
###i for i in mylist if i in ['10', 'K', 'Q', 'L']
    if 'A' in player_cards and [i for i in player_cards if i in ['10','K','Q','J']]:
        game = False
        print("BLACK JACK! you win!")
    elif 'A' in comp_cards and [i for i in comp_cards if i in ['10','K','Q','J']]:
        game = False
        print("BLACK JACK! Computer wins!")
    else:
        player_score += cal_score(player_cards, player_score)
        comp_score += cal_score(comp_cards, comp_score)
        print_cards('Your',player_cards,player_score)
        print_cards('Computer', comp_cards, comp_score)

# print(player_cards,comp_cards)

def take_card():
    card = random.sample(cards, 1)
    return card

def print_cards(player,cards,score):
    if score :
        print(f"{player} score is: {score}")
    else :
        print(f"{player} two cards are {cards}")

def cal_score(cards, score):
    for i in cards:
        if i.isnumeric():
            score += int(i)
        elif i in ['K', 'Q', 'J']:
            score += 10
        elif i == 'A':
            if score + 10 >= 21:
                score += 1
            else:
                score += 10
    return score


def win_lose(f):
    global game
    if player_score >= 21:
        print('you loose :( ')
        game = False
    elif comp_score >= 21:
        print("You  Win!!")
        game = False
    elif player_score > comp_score and f == 1:
        print("You Win!!")
        game = False
    elif player_score < comp_score and f == 1:
        print("You lose!!")
        game = False
    elif player_score == comp_score and f == 1:
        print("DRAW!!")
        game = False


game_start()
# print(cards)

while game:
    opt = input("\nWould you like to take another card or pass? Enter take or pass: ")
    if opt == 'take':
        player_card = take_card()
        player_score = cal_score(player_card, player_score)
        print(f"You took {player_card} and the your score is {player_score}")
        win_lose(0)
        if not game:
            break
        comp_card = take_card()
        comp_score = cal_score(comp_card, comp_score)
        print(f"Computer took {comp_card} and the score for computer is {comp_score}")
        win_lose(0)

    elif opt == 'pass':
        final_comp_card = take_card()
        comp_score = cal_score(final_comp_card, comp_score)
        print(f"Computer took {final_comp_card} and the final score for computer is {comp_score}")
        win_lose(1)
    else:
        print("please enter a valid choice")
