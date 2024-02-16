"""
Coffee Machine Simulator:

This Python script simulates a coffee vending machine that accepts coins for payment. It offers various drinks such as
latte, espresso, and cappuccino. The machine checks the availability of ingredients before preparing the drink.
It also processes the payment and returns change if necessary.

The program consists of three main modules:
- coffee_maker.py: Models the coffee maker and handles the availability of resources.
- menu.py: Models the menu with available drinks and their ingredients.
- money_machine.py: Models the money machine, processing payments and returning change.

Usage:
- Run the main script to start the coffee machine simulator.
- Follow the prompts to select a drink, insert coins, and receive your beverage.
- The machine provides an option to view the current resources available.
- To exit the program, type 'off' when prompted to select a drink.
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Creating instances of the MoneyMachine, CoffeeMaker, and Menu classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Setting a control variable to maintain the main program loop
is_on = True

# Main program loop
while is_on:

    # Getting the list of drink options from the menu
    options = menu.get_items()

    # Asking the user to make a drink choice
    choice = input(f"What would you like? ({options}): ")

    # Checking the user's choice
    if choice == "off":  # If the user chooses 'off', we exit the program
        is_on = False
    elif choice == "report":  # If the user chooses 'report', we display the inventory and money reports
        coffee_maker.report()
        money_machine.report()
    else:  # Otherwise, the user made a drink choice

        # Finding the chosen drink in the menu
        drink = menu.find_drink(choice)

        # Checking if there are enough resources to make the chosen drink and if payment is successfully made
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

            # Making the chosen drink
            coffee_maker.make_coffee(drink)
