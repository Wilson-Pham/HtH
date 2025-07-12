def task_2():
    numbers = [8, -1, -10, 0, 15] # List of numbers to check
    for number in numbers: # Loop through each number in the list
        if number > 0: # Check if the number is positive
            print(f"{number} is a positive number.") # Print a message if positive
        elif number < 0: # Check if the number is negative
            print(f"{number} is a negative number.") # Print a message if negative
        else: # If the number is neither positive nor negative
            print(f"{number} is zero.") # Print a message if zero

            # Print Message:    8 is a positive number.
                                # -1 is a negative number.
                                # -10 is a negative number.
                                # 0 is zero.
                                # 15 is a positive number.

def task_3():
    inventory = ["coal", "iron", "gold", "diamond", "emerald"] # List of items in the inventory
    for block in inventory: # Loop through each item in the inventory
        print(f"You found a block of {block}.") # Print a message for each item found
        if block == "diamond": # Check if the item is a diamond
            print("JACKPOT! You found a diamond!") # Print a special message if a diamond is found
            # Print message:      You found a block of coal.
                                # You found a block of iron.
                                # You found a block of gold.
                                # You found a block of diamond.
                                # JACKPOT! You found a diamond!
                                # You found a block of emerald.

continue_checking = "yes"  # Initialize the variable to control the loop

while continue_checking.lower() == "yes":  # Loop until the user decides to stop
    age = int(input("Enter your age: "))  # Get the age input

    if age >= 18:  # Check if the user is eligible to vote
        print("You are eligible to vote.")  # Message if eligible
        task_2()
        task_3()
    else:  # If not eligible
        print("You are not eligible to vote.")  # Message if not eligible
    
    # Ask if the user wants to check another age
    continue_checking = input("Do you want to check another age? (yes/no): ")
    
