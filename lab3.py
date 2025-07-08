food = "Orange Chicken"

print(food[0:3]) # Prints "Ora", first three characters
print(food[-4:]) # Prints "cken", last four characters

first_last = food[0] + food[-1] # Concatenates (combines) first and last characters

print(first_last) # Prints "On", first and last characters of each string

food_list = food.split() # Splits the string into a list of words
print(food_list) # Prints the list of words in the food string, ['Orange', 'Chicken']

joined_food = " " .join(food_list) # Joins the list of words back into a string with spaces
print(joined_food) # Prints "Orange Chicken", the original food string

number_list = [1, 4, 9, 16, 25, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
number_list.append(441) # Appends (add) 441 to the end of the list
print(number_list) # Prints the updated list with 441 added: [1, 4, 9, 16, 25, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441]

number_list.insert(6,36) # Inserts "36" at index 6, replaces 49 and everything affter it shifts right by 1
print(number_list) # Prints the updated list with 36 inserted at idex 6: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441]

number_list.pop() # Removes the last element (441) from the list
print(number_list) # Prints the updated list with 441 removed: [1, 4, 9, 16, 25, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

number_list.remove(number_list[1]) # Removes the element at idex 1 (4) from the list, also inside the () "number_list[1]" is not needed, you can just use the value 4
print(number_list) # Prints the updated list with 4 removed: [1, 9, 16, 25, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
print(number_list[:3]) # Prints the first three elements of the list: [1, 9, 16]
print(number_list[-3:]) # Prints the last three elements of the list: [324, 361, 400]

books = {"Jeff Kinney": "Diary of a Wimpy Kid", 
         "Kazu Kibuishi": "Amulet", 
         "Rick Riordan": "Percy Jackson and the Olympians", 
         "Lauren Tarshis": "I Survived"} 
print(books.keys()) # Prints the keys of the dictionary: dict_keys(['Jeff Kinney', 'Kazu Kibuishi', 'Rick Riordan', 'Lauren Tarshis'])
print(books.values()) # Prints the values of the dictionary: dict_values(['Diary of a Wimpy Kid', 'Amulet', 'Percy Jack and the Olympians', 'I survived'])

print(books.get("Jeff Kinney")) # Prints the value associated with the key "Jeff Kinney": "Diary of a Wimpy Kid"

books.pop("Rick Riordan")
print(books)

del books[list(books.keys())[0]] # Deletes the first key-value pair in the dictionary
print(books) # Prints the updated dictionary after deleting the first key-value pair: {'Kazu Kibuishi': 'Amulet', 'Lauren Tarshis': 'I Survived'}

