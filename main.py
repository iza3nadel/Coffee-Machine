from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

power_on = True

def calc_value(quarters, dimes, nickles, pennies):
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

while power_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    elif choice == "off":
        power_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        print("Invalid choice. Try again.")






























def check_res(drink, res, menu):
    """If resources are sufficient returns True, otherwise returns False"""
    for key in menu[drink]["ingredients"]:
        if res[key] < menu[drink]["ingredients"][key]:
            return f"Sorry there is not enough {key}."
    return ""



def update_res(drink, res, menu):
    for key in menu[drink]["ingredients"]:
        res[key] -= menu[drink]["ingredients"][key]



money = 0
power_on = True

while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if not check_res(choice, resources, MENU) == "":
            print(check_res(choice, resources, MENU))
        else:
            print("Please insert coins")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            if MENU[choice]["cost"] > calc_value(quarters,dimes, nickles, pennies):
                print("Sorry that's not enough money. Money refunded.")
            else:
                if MENU[choice]["cost"] < calc_value(quarters,dimes, nickles, pennies):
                    change = round(calc_value(quarters,dimes, nickles, pennies) - MENU[choice]["cost"], 2)
                    print(f"Here is ${change} dollars in change.")
                update_res(choice, resources, MENU)
                money += MENU[choice]["cost"]
                print(f"Here is your {choice}. Enjoy!")
    elif choice == "off":
        power_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}ml \nMoney: ${money}")
    else:
        print("Invalid choice. Try again.")