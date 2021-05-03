from art import LOGO
from data import *


def report_generate():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")


def enough_resources(name):
    for ingredient in MENU[name]['ingredients']:
        if MENU[name]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coin():
    total_amount = 0
    print("Please insert coins.")
    for coin in coin_value:
        coin_count = int(input(f"How many {coin}?"))
        total_amount += coin_count * coin_value[coin]
    return total_amount


def is_transaction_successful(name, user_credit):
    if user_credit < MENU[name]["cost"]:
        print("That is not enough money. Money refunded.")
        return False
    else:
        resources['money'] += MENU[name]["cost"]
        user_credit -= MENU[name]["cost"]
        return True


def make_coffee(name):
    for ingredient in MENU[name]['ingredients']:
        resources[ingredient] -= MENU[name]['ingredients'][ingredient]

    print(f"Here is your {name}. Enjoy!")


def start(name):
    if enough_resources(name):
        user_credit = process_coin()
        if is_transaction_successful(name, user_credit):
            print(f"Here is ${user_credit} in change.")
            make_coffee(name)


print(LOGO)

# User prompt
while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        exit()
    elif user_choice == "print":
        report_generate()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        start(user_choice)

