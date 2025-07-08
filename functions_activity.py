menu = {"Pizza": 2.99, 
        "Burger": 3.99,
        "Hot dog": 1.99, 
        "Cheese": 0.59, 
        "Ice cream": 1.49, 
        "Churro": 0.79, 
        "Soda": 0.89}

def total_price(item1, item2):
    total_sum = menu[item1] + menu[item2]
    return total_sum

print(total_price("Pizza", "Burger"))

def price_difference(item3, item4):
    prince_difference = menu[item3] - menu[item4]
    return prince_difference

print(price_difference("Hot dog", "Cheese"))

def inflation(original_price, inflation_rate):
    inflation_rate = 0.05
    inflation_prices = original_price * (1 + inflation_rate)
    return inflation_prices

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