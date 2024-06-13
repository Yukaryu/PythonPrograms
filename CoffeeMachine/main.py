""" GUIDE - HOW TO USE THE COFFEE MACHINE?
answer the prompt by:
drink name (espresso/ latte/ cappuccino) for drink
report for inventory and profits
restock to replenish the inventory to its original levels. money cut from profits.
off to switch off the coffee machine
last three are hidden commands only known by management."""

Menu = {
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
    "profit": 0
}
''' water and milk are in ml, coffee in grams and profit in $'''

#TODO: 2) Generate a report.
def report():
    if agenda == "report":
        for key, values in resources.items():
            print(key.capitalize(), ":", values)


'''The items() method returns a view object. 
        The view object contains the key-value pairs of the dictionary, 
        as tuples in a list. The view object will reflect any changes done 
        to the dictionary
        car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    x = car.items()
    print(x) 
will return:  dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])'''
#TODO: 3) Turn coffee machine off by hidden reply "off" to the prompt.
#TODO: 4) Check resources sufficient.


'''for key, value in Menu.items():
    # this should print the drinks and cost
    print(key, value["cost"])
    # this should print the ingredients
    for key_i, value_i in value["ingredients"].items():
        print(key_i, value_i)'''


def restock():
    global resources
    water_cost = (2.19 / 1500) * (300 - resources["water"])
    milk_cost = (1.05 / 1000) * (200 - resources["milk"])
    coffee_cost = (4.89 / 1000) * (24 - resources["coffee"])
    restocking_cost = water_cost + milk_cost + coffee_cost
    if resources["profit"] >= restocking_cost:
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "profit": resources["profit"] - restocking_cost
        }
        print("Restocked.")
    else:
        print("Not sufficient money to restock.")

    ''' In USA, 1.5 l bottled water costs 2.19$ avg, 1 l milk costs 1.05$ according to 
    https://www.numbeo.com/cost-of-living/country_price_rankings?itemId=13
    and 1 kg of coffee costs 4.89 $ according to
    https://markets.businessinsider.com/commodities/coffee-price
    .'''


def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            print("Resources sufficient. Processing order.")
            return True


#TODO: 5) Process coins.
def process_coins(order_cost, drink_name):
    print(drink_name.capitalize(), "costs $", order_cost, ".")
    print("Please insert coins:")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    amt_paid = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    if amt_paid < order_cost:
        print("Transaction unsuccessful. Money refunded. You need to pay $", order_cost - amt_paid, "more.")
        return False
    elif amt_paid > order_cost:
        resources["profit"] += order_cost
        print("Transaction successful. Your change is $", amt_paid - order_cost, ".")
        print(f"Here is your {drink_name} ☕! Enjoy!!!")
        return True
    else:
        resources["profit"] += order_cost
        print("Transaction successful.")
        print(f"Here is your {drink_name} ☕! Enjoy!!!")
        return True


#TODO: 6) Check transaction successful. Return change.
#TODO: 7) Make coffee. Deduct resources.
def deduct_resources(order_item):
    for item in order_item:
        resources[item] -= order_item[item]
    return


is_on = True
while is_on:
    # TODO: 1) "What would you like? (espresso/latte/cappuccino): ” prompt
    agenda = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if agenda == "report":
        report()
    elif agenda == "off":
        is_on = False
    elif agenda == "restock":
        # TODO: 8) Buy resources and replenish stock.
        restock()

    else:
        drink = Menu[agenda]
        if resources_sufficient(drink["ingredients"]):
            process_coins(drink["cost"], agenda)
            deduct_resources(drink["ingredients"])
