# Lab 5 Wilson Pham

def cat_greeting(word): # Function to greet with a word
    print(f"Cat says {word}!") # Prints the greeting
    print("Cat sees Wilson!") # Prints a message about seeing Wilson
 
cat_greeting("Meow") # Calling the function with "Meow"

# Printed messages: "Cat says Meow!" and "Cat sees Wilson!"

def generate_superhero_power(): # Function to generate a superhero power
    name = "Wilson" # Name of the superhero
    power = "invisibility" # Superpower of the superhero
    print(f"{name} has the power of {power}!") # Prints the superhero's name and power

# Printed messages: "Wilson has the power of invisibility!"

generate_superhero_power() # Calling the function to generate superhero power

def generate_superhero_power1(): # Function to generate a superhero power
    power = "Super Strength" # Superpower of the superhero
    return power # Returns the superpower

print(generate_superhero_power1()) # Printed message: "Super Strength"

def generate_superhero_power2(user_name, super_power): # Function to generate a superhero power with user input
    message = user_name + " has the power of " + super_power + "!" # Constructs a message with the user's name and superpower
    return message # Returns the constructed message

print(generate_superhero_power2("Wilson", "Super Speed")) # Printed message: "Wilson has the power of Super Speed!"

def cat_greetings_loop(greeting): # Function to print cat greetings in a loop
    for i in range(5): # Loop to repeat the greeting 5 times
        print(f"Cat says {greeting}") # Prints the greeting each time

cat_greetings_loop("Meow") # Printed message: "Cat says Meow" five times

def generate_multiple_powers(): # Function to generate multiple superhero powers
    superpowers = ["Flying", "Invisibility", "Super Strength", "Telepathy"] # List of superhero powers
    for i in superpowers: # Loop through each superpower in the list
        print(f"Superpower: {i}") # Prints each superpower

generate_multiple_powers() # Calling the function to print multiple superhero powers
