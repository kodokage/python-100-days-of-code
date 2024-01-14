menu  = {
    "expresso" : {
        "water" : 100,
        "coffee": 18,
        "cost" : 1.5,
    },

     "latte" : {
        "water" : 200,
        "coffee": 24,
        "milk" : 150,
        "cost" :2.4,
    },
     "cappuccino" : {
        "water" : 250,
        "milk": 100,
        "coffee": 18,
        "cost" : 3.0,
    }
}

# print(menu["expresso"]["cost"])
resources = {
    "water": 300,
    "milk": 200,
    "coffee" : 100,
    "money":0
}

## Currency worth
penny = 0.01
nickel = 0.05
dime =  0.10
quarter = 0.25


# TODO : process money
def process_coins():
    print("Please insert coins")
    pennies = penny * int(input("How many pennies ? : ")) 
    nickels = nickel * int(input("How many nickels ? : ")) 
    dimes = dime * int(input("How many dimes ? : ")) 
    quarters = quarter * int(input("How many quarters ? : "))  
    total  = pennies + nickels + dimes + quarters
    return total

#TODO : handle orders
def order_handling(order):
 
    if (amount <  menu[order]["cost"]):
        print("Sorry, that's not enough money. Money refunded. ")
    else:
        if( (menu[order]["water"] > resources["water"]) or  (menu[order]["coffee"] > resources["coffee"]) ):
            print("Sorry, one of the ingredients is insufficient")
            print("Reload machine and restart")
            
        else:
            resources["water"] = resources["water"] - menu[order]["water"]
            # resources["milk"] = resources["milk"] - menu[order]["milk"]
            resources["coffee"] = resources["coffee"] - menu[order]["coffee"]
            resources["money"] = resources["money"] + menu[order]["cost"]
            print(resources)
            change = amount -  menu[order]["cost"]
            print(f" Here's your {change} in change")
            print(f"Here's your {order}, enjoy")
            

# TODO : print the resources
            
order = ""
while order != "off":

    order = input("What would you like to order? (expresso/latte/cappuccino) : ").lower()

    ## Print inventory report
    if(order == "report"):
        print(resources)
    elif(order == "off"):
        print("Loggin off....")
        break
    else:
        print(f"That will be # {menu[order]['cost']}")
        amount = process_coins()
        order_handling(order)
   