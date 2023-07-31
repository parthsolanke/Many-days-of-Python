from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0
on = True
items = Menu()
barista = CoffeeMaker()
cashier = MoneyMachine()

while on:
    choice = input(f"What would you like? ({items.get_items()}):")
    if choice == "off":
        on = False
    elif choice == "report":
        barista.report()
        cashier.report()
    else:
        drink = items.find_drink(choice)
        if barista.is_resource_sufficient(drink) and cashier.make_payment(drink.cost):
                barista.make_coffee(drink)