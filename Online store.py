"""
    COSC 1306 - Fall 2017

        First mame: Awais
        Last name: Ahmed
        PeopleSoftID: 1776344

    Program #1: Shopping cart

GENERAL INSTRUCTIONS:

- Your code has to be in between the pair of long lines with #######
- Do not edit the prints, specially the last one since the evaluator uses that to give you a grade
- The tabulation of the code should not change (and this can give you hints!)
- Do not forget to fill the comments above with your information
"""

total_bill = 0

print("============================================")
print("\tWelcome to UH Online Store")
print("============================================\n")

market_item1, market_price1, market_stock1, user_quantity1 = "Milk box", 1.99, 10, 0
market_item2, market_price2, market_stock2, user_quantity2 = "Chickpeas", 1.59, 100, 0
market_item3, market_price3, market_stock3, user_quantity3 = "Cereal", 2.99, 150, 0

####################################################################
### YOUR CODE: add an infinite loop to keep asking the user for products
loopOne = 1
while loopOne != 0:
    ####################################################################

    print("\tItem\tPrice\tStock")
    print("1) {}\t{}\t{}".format(market_item1, market_price1, market_stock1))
    print("2) {}\t{}\t{}".format(market_item2, market_price2, market_stock2))
    print("3) {}\t{}\t{}".format(market_item3, market_price3, market_stock3))
    print("\nNegative quantities will remove items from your cart.")
    print("Press 0 to finish shopping.")
    item_num = int(input("Provide the item number: "))
    while item_num > 3 or item_num < 0:
        item_num = int(input(" Invalid Input \nProvide the item number: "))
    if item_num == 1 or item_num == 2 or item_num == 3:

        ####################################################################
        ### YOUR CODE: ask the user for the item number choice

        ####################################################################

        ####################################################################
        ### YOUR CODE: break the infinite loop when 'item_num' is zero
        ####################################################################

        ####################################################################
        ### YOUR CODE: choose the corresponding values based on the 'item_num'
        ###            For instance, if item 1 is chosen, set market_stock with
        ###            market_stock1 and so on and so forth for all items
        if item_num == 1:
            market_item = 1
            market_stock = market_stock1
            market_price = market_price1
            user_quantity = user_quantity1
        elif item_num == 2:
            market_item = 2
            market_stock = market_stock2
            market_price = market_price2
            user_quantity = user_quantity2
        elif item_num == 3:
            market_item = 3
            market_stock = market_stock3
            market_price = market_price3
            user_quantity = user_quantity3
        else:
            print("Invalid input")
        ####################################################################

        ####################################################################
        ### YOUR CODE: Ask the user for a quantity value. If the quantity can be satisfied,
        ###            then the quantity is valid. Otherwise, the program should ask for
        ###            valid quantity again (up to 3 times). On the third time of invalid
        ###            quantity, the program should assign to the item_qty variable the
        ###            available number of items. If the number is negative, it should be
        ###            the available number of items in the cart. If the number is positive,
        ###            it should be the available number of items in the stock. Remember that
        ###            you need to inform the user of what happens.
        item_qty = int(input("Provide the quantity for item"))
        while item_qty < 0 and item_qty * - 1 > user_quantity:
            item_qty = int(input("Try again"))
        if item_qty <= market_stock:

            if item_qty > 0:
                market_stock = market_stock - item_qty
            else:
                market_stock = market_stock - item_qty
        else:
            tries = 2
            while tries != 0 and item_qty > market_stock:
                print("Not enough stock is available")
                item_qty = int(input("Provide the quantity for item"))
                tries = tries - 1
                if item_qty <= market_stock:
                    market_stock = market_stock - item_qty

            item_qty = market_stock
            market_stock = market_stock - item_qty

            ####################################################################

        ####################################################################
        ### YOUR CODE

        user_quantity += item_qty
        # market_stock = market_stock - user_quantity
        if user_quantity > 0:
            total_bill = total_bill + market_price * item_qty
        else:
            total_bill = total_bill - market_price * item_qty
        ####################################################################

        ####################################################################
        ### YOUR CODE: only one of the 3 following prints is executed at a time.
        ###            Add the if, elif, else conditions as needed.
        if item_qty > 0:
            print("\nAdding '{}' (${:.2f} x {}) to your cart".format(market_item, market_price, item_qty))
        elif item_qty < 0:
            print("\nRemoving '{}' (${:.2f} x {}) from your cart".format(market_item, market_price, item_qty))
        else:
            print("\nNothing will be added or removed for item #{}.".format(item_num))
        ####################################################################

        print("Cart total: ${:.2f}\n".format(total_bill))  # DO NOT CHANGE THIS LINE

        # The code below updates the original stock and user's cart variables
        if item_num == 1:
            market_stock1 = market_stock
            user_quantity1 = user_quantity
        elif item_num == 2:
            market_stock2 = market_stock
            user_quantity2 = user_quantity
        elif item_num == 3:
            market_stock3 = market_stock
            user_quantity3 = user_quantity

        print("============================================\n")

    else:
        loopOne -= 1

print("\nYour total is ${:.2f}".format(total_bill))
print("\nThanks for shopping at UH")

