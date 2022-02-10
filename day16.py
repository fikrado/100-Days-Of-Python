from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money = MoneyMachine()
coffe = CoffeeMaker()
menu = Menu()
menuitem = MenuItem


is_on = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino/)\n =>")
    if choice == "off":
        is_on = False

    elif choice == "report":
        money.report()
        coffe.report()

    else:
          drink = menu.find_drink(choice)
          if coffe.is_resource_sufficient(drink) and money.process_coins():
              coffe.make_coffee(drink)






