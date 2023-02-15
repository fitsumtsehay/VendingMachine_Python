#@ VendingMachine_Python
A Python program that simulates the operations of a vending machine with four functions:
1. Display menu
2. Take cash
3. Offer products
4. Return change in coins

##@ The program will perform the following in order:
1) Display the instructions to the user
2) Take in money from the user
3) Display the menu of products
4) Offer the products
5) Retrieve products selected, and remaining balance
6) Dispense products
7) Return change in coins

### Functions and Requirements
- Display the Menu
  - Parameter: menu
  - Return: none
- This function takes in the dictionary menu and displays the key and values in one
line. For example, the menu variable above contains the key 101, and the value is
a list that contains two elements, ‘Snickers Bar’ and 0.88. Thus, your will pass the
dictionary into this function as an argument, and display the information in this
order:

### Take Cash
- Parameter: none
- Return: balance
- This function will repeatedly ask the user to enter bills or coins. When the user
presses 0, function will return the balance (total of all money collected)
- Only the following values are accepted: 0.05, 0.10, 0.25, 1, 5. If the user inputs a
value other than accepted values, display the message “>> Invalid Input. Try
Again!”
- Values are accepted one at a time. That is, one coin or bill at a time.
- Keep asking the user to input values, and adding inserted cash into the total, until
the user presses 0. Then, return the balance.
- This function, displays a message (print()) AND returns a value (return). So, call
this function inside a variable to store the returned value, balance.

### Offer Products
- Parameter: balance
- Return: selected products, remaining balance
- Before running this function, call the function that displays the menu first.
- This function takes in the balance as an argument, then asks the user to select a
product.
- The user will use the product’s code in order to make as selection. Each time the
user selects a product, the price of that product is deducted from the balance, and
the product is added into a list.
- Each time the user selects a product, check if the balance is sufficient, that is, the
current balance is larger than the price of the item. If the item chosen has a price
higher than the balance, display the message “Insufficient balance.”
- The user will continue to select products until 0 is pressed. When the user presses
the function returns the selected products, and the remaining balance.

### Get Change
- Parameter: amount
- Return: quarters, dimes, nickels, and pennies
- This function will take in the remaining balance as an argument, and return the
change in coins.
- The remaining balance will be passed into the function in dollars. Before doing
the operations, convert the balance into cents by multiplying it by a 100.
- The change will be given from starting with the highest coin denomination
possible. For instance, if the remaining balance is 0.76, the change will be 3
quarters and a penny.
