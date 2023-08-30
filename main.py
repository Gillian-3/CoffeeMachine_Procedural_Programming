# TODO: 2.CHECK RESOURCES SUFFICIENT TO MAKE DRINK ORDER
MENU = {
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
    "cost": 0
}


# TODO: 1.PRINT A REPORT OF ALL THE COFFEE MACHINE RESOURCES
def report():
    for j in resources:
        print(j, resources[j])


i = 1
while i == 1:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        i = 2
    elif order == "report":
        report()
    elif order == "espresso":
        if resources["water"] < 50:
            print("Sorry there is not enough water")
        elif resources["coffee"] < 18:
            print("Sorry there is not enough coffee")
        else:
            print("Insert coins:")
            q1 = int(input("number of quarter: "))
            q2 = int(input("number of dimes: "))
            q3 = int(input("number of nickel: "))
            q4 = int(input("number of pennies: "))
            q = q1 * 0.25 + q2 * 0.1 + q3 * 0.05 + q4 * 0.1
            if q >= MENU[order]["cost"]:
                resources["cost"] += MENU[order]["cost"]
                if q > MENU[order]["cost"]:
                    r = q - MENU[order]["cost"]
                    print(f"Here is ${r} dollars in change. ")
                print("Thankyou for the purchase")

                resources["water"] -= 50
                resources["coffee"] -= 18
            else:
                print("Sorry that's not enough money. Money refunded")

    elif order == "latte":
        if resources["water"] < 200:
            print("Sorry there is not enough water")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee")
        elif resources["milk"] < 150:
            print("Sorry there is not enough milk")
        else:
            print("Insert coins:")
            q1 = int(input("number of quarter: "))
            q2 = int(input("number of dimes: "))
            q3 = int(input("number of nickel: "))
            q4 = int(input("number of pennies: "))
            q = q1 * 0.25 + q2 * 0.1 + q3 * 0.05 + q4 * 0.1
            if q >= MENU[order]["cost"]:
                resources["cost"] += MENU[order]["cost"]
                if q > MENU[order]["cost"]:
                    r = q - MENU[order]["cost"]
                    print(f"Here is ${r} dollars in change. ")
                print("Thankyou for the purchase")
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"] -= 150
            else:
                print("Sorry that's not enough money. Money refunded")
    elif order == "cappuccino":
        if resources["water"] < 250:
            print("Sorry there is not enough water")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee")
        elif resources["milk"] < 100:
            print("Sorry there is not enough milk")
        else:
            print("Insert coins:")
            q1 = int(input("number of quarter: "))
            q2 = int(input("number of dimes: "))
            q3 = int(input("number of nickel: "))
            q4 = int(input("number of pennies: "))
            q = q1 * 0.25 + q2 * 0.1 + q3 * 0.05 + q4 * 0.1
            if q >= MENU[order]["cost"]:
                resources["cost"] += MENU[order]["cost"]
                if q > MENU[order]["cost"]:
                    r = q - MENU[order]["cost"]
                    print(f"Here is ${r} dollars in change. ")
                print("Thankyou for the purchase")
                resources["water"] -= 250
                resources["coffee"] -= 24
                resources["milk"] -= 100
            else:
                print("Sorry thats not enough money. Money refunded")
