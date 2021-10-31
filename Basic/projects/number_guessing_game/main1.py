from random import randint
again = True
while(again):
    winning_number = randint(1,100)

    logo = """
      / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
     / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
    / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
    """
    print(logo)
    print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")
    a = input("Choose your difficulty : ")

    if (a == "hard"):
        attempts = 3
        print(f"you have {attempts} attempts")

        while(attempts):
            g = int(input("can you guess the winning number? "))
            if g < winning_number :
                print("Number is too low ")
            if g > winning_number:
                print("Number is too high ")
            if g == winning_number:
                print("Congratulations you won! ")
            attempts -= 1
        print("Out of attempts")

    if (a == "easy"):
        attempts = 1
        print(f"you have {attempts} attempts")

        while(attempts):
            g = int(input("can you guess the winning number? "))
            if g < winning_number :
                print("Number is too low ")
            if g > winning_number:
                print("Number is too high ")
            if g == winning_number:
                print("Congratulations you won! ")
            attempts -= 1
        print("Out of attempts")

    a = input("You want to play again?: ")
    if (a=='yes'):
        again = True
    else :
        again = False



