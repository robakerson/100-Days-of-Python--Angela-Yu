from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coin_machine = MoneyMachine()
coffee_machine= CoffeeMaker()

# print(coffee_machine.report())

# items = coffee_menu.get_items()
# latte= coffee_menu.find_drink('latte')
#
# print(items)
# print(latte.ingredients)

def process_user_input(input):
    if input == 'off':
        return '', False
    elif input == 'report':
        print(coffee_machine.report())
        coin_machine.report()
        return '', True
    elif input not in coffee_menu.get_items():
        print("I didn't understand your input. Please try again")
        return '', True
    else:
        return input, True


# print(coin_machine.make_payment(2.5))

# print(coffee_menu.find_drink('latte').cost)
#
user_input = input(f"What would you like ({coffee_menu.get_items()})?")
drink, machine_on = process_user_input(user_input)
#
# print(drink)
# print(coffee_machine.is_resource_sufficient(drink))


while machine_on:
    if drink:
        # this is needed to pass to is_resource_sufficient as it requires a Menuitem object and not a string
        drink_to_make = coffee_menu.find_drink(drink)
        if coffee_machine.is_resource_sufficient(drink_to_make):
            drink_cost = coffee_menu.find_drink(drink).cost
            if coin_machine.make_payment(drink_cost):
                coffee_machine.make_coffee(drink_to_make)
                coin_machine.report()
    user_input = input(f"What would you like ({coffee_menu.get_items()})?")
    drink, machine_on = process_user_input(user_input)