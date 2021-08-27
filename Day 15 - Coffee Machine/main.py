MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: create resources report


def get_user_input():
    return input("What would you like? (espresso/latte/cappuccino):")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def process_selection(selection):
    if selection == 'report':
        print_report()
        return '', True
    elif selection == 'off':
        return '', False
    else:
        purchase = selection
        return purchase, True

def insert_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    cash = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return cash

def buy_latte():
    return

money = 0
machine_on = True

while machine_on:
    user_selection = get_user_input()
    coffee_purchased, machine_on = process_selection(user_selection)
    coffee_ingredients = MENU[coffee_purchased]['ingredients']
    print(coffee_purchased)
    print(coffee_ingredients)

# print(MENU['latte']['cost'])
