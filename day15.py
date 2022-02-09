############################################################## DEMO #####################################################

from operator import itemgetter
menu = {
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
}
water = itemgetter('water')(resources)
coffee = itemgetter('coffee')(resources)
milk = itemgetter('milk')(resources)

is_on = True

def check_re():
    if choice == "espresso":
        water - 50
        coffee - 18
        if water == 0:
            print("no water")
        elif coffee == 0:
            print("no coffee")
        elif milk == 0:
            print("no milke")
        else:
            pass

    elif choice == "latte":
        water - 200
        coffee - 24
        milk - 150
        if water == 0:
            print("no water")
        elif coffee == 0:
            print("no coffee")
        elif milk == 0:
            print("no milke")
        else:
            pass

    elif choice == "cappuccino":
        water - 100
        coffee - 24
        milk - 150
        if water == 0:
            print("no water")
        elif coffee == 0:
            print("no coffee")
        elif milk == 0:
            print("no milke")
        else:
            pass
    else:
        pass



while True:
    choice = input("what will u like \nlatte , cappuccino and espresso => ")
    if choice == "off":
        is_on = False

    elif choice== "cappuccino":
        money = True
        while True:
            cost = 0
            cost += int(input("the cost will 1.5\n $"))
            if cost >= 1.5:
                print("thank you and change is ", cost - 1.5)
                money = False
            else:
                print("no enough money")



    elif choice == "latte":
        money = True
        while True:
            cost = 0
            cost += int(input("the cost will 1.5\n $"))
            if cost >= 2.5:
                print("thank you and change is ", cost - 2.5)
                money = False
            else:
                print("no enough money")

    elif choice == "espresso":
        money = True
        while True:
            cost = 0
            cost += int(input("the cost will 1.5\n $"))
            if cost >= 3:
                print(f"enjoy your and change is {choice} ", cost - 3)
                money = False
            else:
                print("no enough money")
    check_re()
    
##################################################   DEMO  ##############################################################
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
############################################### PREFECT ONE IS ##########################################################






############################################### PREFECT ONE IS ##############################################################
