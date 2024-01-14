menu = {
    "expresso": {
        "water": 100,
        "coffee": 18,
        "cost": 1.5,
    },

    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.4,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 18,
        "cost": 3.0,
    }
}

# print(menu["expresso"]["cost"])
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
profit = 0 
import prettytable
def is_resource_sufficient(order_ingredients):
    choice


is_on = True
while is_on:
    choice = input("What would you like? (expresso/latte/cappucino) : ")
    if choice == "off": 
        is_on = False
    elif choice =="report":
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} g")
        print(f"Money : # {profit}")
    else:
        drink = menu[choice]
        is_resource_sufficient(drink)
        print(drink)