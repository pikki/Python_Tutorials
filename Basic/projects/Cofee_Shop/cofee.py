MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

############### CODE STARTS HERE
# Name : Himalaya Kilaru
# Email : himalay.kilaru@gmail.com
# Project : Coffee Shop

################
# defining global variables
machine = True
make_cofee = True

# Printing Coffee types and their respective prices
def offer_menu():
    '''Prints coffee in menu and prices'''
    for coffee in list(MENU):
        print(f"{coffee} : {MENU[coffee]['cost']}$")


def cal_input():
    '''Calculates the total amount entred by the user'''
    q = int(input('Enter quarters:'))
    d = int(input('Enter dimes:'))
    n = int(input('Enter nickels:'))
    c = int(input('Enter cents:'))
    return ((q * 25) + (d * 10) + (n * 5) + c) / float(100)


def check_resource(coffee):
    '''Returns a boolean value if theres enough resource'''
    if MENU[coffee]['ingredients']['water'] >= resources['water'] and MENU[coffee]['ingredients']['milk'] >= resources[
        'milk'] and MENU[coffee]['ingredients']['coffee'] >= resources['coffee']:
        print('Sorry we don\'t have enough resources')
        make_cofee = False
    else:
        make_cofee = True
    return make_cofee


while machine:
    offer_menu()
    coffee = input('What would you like to have : espresso/latte/capuccino ?\nPress 0 to exit ')
    if coffee != '0':
        total_input = cal_input()
        if total_input >= MENU[coffee]['cost'] and check_resource(coffee):
            profit += total_input
            for i in list(MENU[coffee]['ingredients']):
                resources[i] = resources[i] - MENU[coffee]['ingredients'][i]
    else:
        machine = False
print(f'total profit is:{profit}')
print(f'total resource left is :')
print(f"Water: {resources['water']}ml")
print(f"Milk: {resources['milk']}ml")
print(f"Coffee: {resources['coffee']}g")

