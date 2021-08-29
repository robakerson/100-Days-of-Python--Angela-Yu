from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coin_machine = MoneyMachine()
coffee_machine= CoffeeMaker()

# print(coffee_machine.report())
# items = coffee_menu.get_items()
# latte= coffee_menu.find_drink('latte')
# print(items)
# print(latte.ingredients)

# return [drink or nothing/True or False] based on user input.
# First return is nothing if user doesn't input proper drink name
# Second return is False if user turns machine off and True otherwise
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
# user_input = input(f"What would you like ({coffee_menu.get_items()})?")
# drink, machine_on = process_user_input(user_input)
#
# print(drink)
# print(coffee_machine.is_resource_sufficient(drink))

machine_on = True

#machine turns off if user types "off"
while machine_on:
    user_input = input(f"What would you like ({coffee_menu.get_items()})?")
    drink, machine_on = process_user_input(user_input)

    # if user doesn't input proper drink name we don't want to run some of the below code as it will throw errors
    if drink:
        # this is needed to pass to is_resource_sufficient as it requires a Menuitem object and not a string
        drink_to_make = coffee_menu.find_drink(drink)
        # check if coffee_machine has enough ingredients to make desired drink. If not, will say so and go back to start of loop
        if coffee_machine.is_resource_sufficient(drink_to_make):
            # pull "cost" of drink from menu
            drink_cost = coffee_menu.find_drink(drink).cost
            # make_payment will ask user for coins and give change. Returns false if user doesn't give enough $
            if coin_machine.make_payment(drink_cost):
                # deduct ingredients from coffee_machine and print proper message
                coffee_machine.make_coffee(drink_to_make)
