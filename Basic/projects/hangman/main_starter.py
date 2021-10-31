import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
# game_is_finished = False
# lives = len(stages) - 1
chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)

print(chosen_word)

dash_list = ['_'] * len(chosen_word)

stand = stages[-1]

while len(stages) != 1 and (list(chosen_word) != dash_list):
    l = input("\nGuess a letter: ")
    if l in chosen_word_list:
        # print("you guessed a letter right. Guess again")
        dash_list[chosen_word_list.index(l)] = l
        for i in dash_list:
            print(i, end=" ")
        chosen_word_list[chosen_word_list.index(l)] = ''
        print(stages[-1])
    else:
        # print("no you got the letter wrong you lose a life")
        del stages[-1]
        print(stages[-1])

# lose
if not stages:
    print("\nYou are dead!")
# win
if list(chosen_word) == dash_list:
    print("\nTop notch!")
