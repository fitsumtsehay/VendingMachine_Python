
"""
---Each Have their own code---
101. Snickers Bar           ($0.88)
102. Clif Bar               ($1.99)
103. Pop-Tart               ($0.76)
104. Doritos Chips         ($2.50)
105. Planters Trail Mix   ($3.25)
106. Snydes Pretzels   ($2.98)

201. Dasani Water Bottle   ($1.50)
202. Monster Energy Drink  ($3.00)
203. Starbucks Cold Coffee  ($3.25)
204. Pepsi                  ($2.00)
205. Diet Pepsi             ($2.00)
206. Gatorade               ($2.00)

display_menu()
take_cash()
offer_product()
get_change()


"""
instructions = """
----------------------------INSTRUCTIONS---------------------------------
>> We Accept $1, $5, and Coins (Quarters 0.25, Dimes 0.10, Nickels 0.05)
>> Insert One Bill/Coin at a Time. Then, Press 0 to Select a Product
------------------------------------------------------------------------
"""

menu = {101: ('Snickers Bar', 0.88), 102: ('Clif Bar', 1.99), 103: ('Pop-Tart', 0.76),
        104: ('Doritos Chips', 2.50), 105: ('Planters Trail Mix', 3.25), 106: ('Snyders Pretzels', 2.98),
        201: ('Dasani Water Bottle', 1.50), 202: ('Monster Energy Drink', 3.00), 203: ('Starbucks Cold Coffee', 3.25),
        204: ('Pepsi', 2.00), 205: ('Diet Pepsi', 2.00), 206: ('Gatorade', 2.00)}


def display_menu(menu):
    print('--'*20)
    print('|CODE |-------PRODUCT NAME-------| PRICE')
    for key in menu:
        name = menu[key][0]
        price = menu[key][1]
        print('| {} | {:<24} |${}'.format(key,name,price))
    print('--' * 20)


def take_cash():
    accepted = [0.05, 0.10, 0.25, 1, 5]
    balance = 0
    while True:
        cash = float(input(' | Balance ${:<5}| Please Enter Bill or Coin (or press 0 to continue): '.format(balance)))
        if cash == 0:
            break
        elif cash in accepted:
            balance += cash
        else:
            print('\t>>Invalid Input. Try Again!')
    return round(balance, 2)


def offer_product(balance):
    current_balance = balance
    selected_products = []
    while True:
        selection = int(input(f'|Balance ${round(current_balance,2)}| Enter Product Code (or press 0 to continue):'))
        if selection == 0:
            break
        elif selection in menu:
            if current_balance > menu[selection][1]:
                selected_products.append(menu[selection][0])
                current_balance -= menu[selection][1]
            else:
                print('\t>>Insufficient balance.')
        else:
            print('\t>>Invalid input. try again!')
    return selected_products, round(current_balance*100, 2)


def get_change(amount):
    quarters = int(amount // 25)
    amount = amount % 25
    dimes = int(amount // 10)
    amount = amount % 10
    nickels = int(amount // 5)
    amount = amount % 5
    pennies = int(amount)
    return quarters, dimes, nickels, pennies

# ----------- PROGRAM RUNS HERE ------------
# 1) display instructions
print(instructions)
# 2) take in money
balance = take_cash()
# 3) display menu
display_menu(menu)
# 4) offer products
dispense = offer_product(balance)
# 5) retrieve products selected, and remaining balance
products_selected = dispense[0]
remaining_balance = dispense[1]
# 6) dispense product and return change in coins
change = get_change(remaining_balance)
print('\n')
print('--'*20)
print('Dispensing Product: ', products_selected)
print(f'Dispensing Change: {change[0]} quarters, {change[1]} dimes, {change[2]} nickels, {change[3]} pennies')