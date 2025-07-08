menu = {"Pizza": 2.99, 
        "Burger": 3.99,
        "Hot dog": 1.99, 
        "Cheese": 0.59, 
        "Ice cream": 1.49, 
        "Churro": 0.79, 
        "Soda": 0.89}

def total_price(item1, item2): # Function that gets the total price of items 1 and 2
    total_sum = menu[item1] + menu[item2] # item 1 + item 2
    return total_sum # Returns added value of items 1 and 2 together

print(total_price("Pizza", "Burger")) # Prints total price annd item 1 and 2: 6.98

def price_difference(item1, item2): # Function that gets the price difference of items 1 and 2
    price_difference = abs (menu[item1] - menu[item2]) # item 1 - item 2; which is a negative number, but using abs, it makes the number positive
    return price_difference # Returns difference value of items 1 and 2

print(price_difference("Pizza", "Burger")) # Prints price difference between item 1 and 2: 1.0 (-1.0 if abs wasn't included)

def inflation(menu, inflation_rate): # Function that inflates the price of all items by a value
    return {item: price * inflation_rate for item, price in menu.items()} # Returns items 1-6, newly inflated values

new_menu = inflation(menu, 1.5) # Calls the function 
print(new_menu) # Prints the inflated (1.5) price of all items: {'Pizza': 4.485, 'Burger': 5.985, 'Hot dog': 2.985, 'Cheese': 0.885, 'Ice cream': 2.235, 'Churro': 1.185, 'Soda': 1.335}

def deflation(original_price, deflation_rate): # Function that deflates the prices of all items by a value
    return {item: price / deflation_rate for item, price in menu.items()} # Returns items 1-6, newly deflated values

new_menu1 = deflation(menu, 1.5) # Calls the function
print(new_menu1) # Prints the deflated (1.5) price of all items: {'Pizza': 1.9933333333333334, 'Burger': 2.66, 'Hot dog': 1.3266666666666667, 'Cheese': 0.3933333333333333, 'Ice cream': 0.9933333333333333, 'Churro': 0.5266666666666667, 'Soda': 0.5933333333333334}

def exponential_growth(menu, growth_rate, periods): # Function that exponentially increases the prices of all items 
    return {item: price * (growth_rate ** periods) for item, price in menu.items()} # Returns items 1-6 exponential values after certain periods: menu * expon.^yr

new_menu = exponential_growth(menu, 1.5, 5) # Calls the function
print(new_menu) # Prints the exponential growth (1.5) prices of all items in 5 years:{'Pizza': 22.7053125, 'Burger': 30.2990625, 'Hot dog': 15.1115625, 'Cheese': 4.4803125, 'Ice cream': 11.3146875, 'Churro': 5.9990625, 'Soda': 6.7584375}

print(inflation(2.99, 0.05))

def deflation(original_price, deflation_rate):
    deflation_rate = 0.5
    deflation_prices = original_price * (1 - deflation_rate)
    return deflation_prices

print(deflation(3.99, 0.5))

def exponential_growth(original_price, growth_rate, years):
    growth_rate = 0.1
    exponential_growth_price = original_price * ((1 + growth_rate) ** years)
    return exponential_growth_price

print(exponential_growth(1.49, 0.1, 5))