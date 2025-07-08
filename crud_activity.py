cookbook = []

def create(recipe): # This function creates a new recipe and adds it to the cookbook
    cookbook.append(recipe) # This function adds a new recipe to the cookbook
    print(f"Recipe {recipe} added successfully.") # Prints a success message

def read(index): # This function reads a recipe at a given index
     if 0 <=index < len(cookbook): # Checks if the index is valid
        return cookbook[index] # Returns the recipe at the specified index
     else:
        print("please enter a valid index.") # Prints an error message if the index is invalid

def update(index, new_recipe): 
    if 0 <= index < len(cookbook): # This function updates a recipe at a given index with a new recipe
        print(f"Recipe at index {index} updated to: {new_recipe}.") # Prints a success message
        cookbook[index] = new_recipe # Updates the recipe at the specified index with the new recipe
    else: # If the index is invalid, prints an error message
        print("Please enter a valid index.") # Prints an error message if the index is invalid
        index = input("Enter the index of the recipe to update: ") # Gets the index from the user
        new_recipe = input("Enter the name of the recipe you want to update it with: ") # Gets the new recipe name from the user
        index = int(index) # Converts the index to an integer
        update(index, new_recipe) # Recursively calls the update function with the new index and recipe name

 
def destroy(index): # This function deletes a recipe at a given index
    if index < len(cookbook): # Chhecks if the index is valid
        destroy = cookbook.pop(index) # Removes the recipe at the specified index
        print(f"Recipe {destroy} removed successfully.") # Prints a success message
    else: # If the index is invalid, prints an error message
        print("Please enter a valid index.") # Prints an error message if the index is invalid

def list_all_recipes(): # This function lists all recipes in the cookbook
    print("Listing all recipes:") # Prints a header for the list of recipes
    for i, recipe in enumerate(cookbook): # Enumerates through the cookbook to get both index and recipe
        print(f"{i}: {recipe}") # Prints the index and recipe name

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            new_recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, new_recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main() 
# This code implements a simple CRUD (Create, Read, Update, Delete) application for managing a cookbook.
# It allows users to add, read, update, delete, and list recipes.


        