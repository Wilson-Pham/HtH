# Debugging Activity - Wilson Pham

# Problem 1: y was equal to 0, which caused a ZeroDivisionError (undefined).
x = 10
y = 2
result = x / y # ZeroDivisionError
print("Result:", result)

# Problem 2: i + 1 was used and caused an IndexError because it tried to access an index that was out of range and skipped first index
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i]) # IndexError: list index out of range

# Problem 3: forgot ":"
def calculate_area(radius): # SyntaxError: Missing colon
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

# Problem 4: forgot ":"
def is_even(number):
   if number % 2 == 0: # SyntaxError: Missing colon
       return True
   else: # SyntaxError: Missing colon
       return False
 
print(is_even(4))
print(is_even(7))

# Problem 5: forgot ":"
for i in range(5): # SyntaxError: Missing colon
   print(i)

# Problem 6: Missing + 
def greet(name):
   return "Hello, "+ name + "!" # SyntaxError: Missing concatenation operator
 
print(greet("Alice"))

# Problem 7: missing indentation
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number # IndentationError: expected an indented block
print("Sum of numbers:", sum)

# Problem 8: No errors
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1) 
 
print(factorial(5))

# Problem 9: Missing "name ==" before Bob
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": # Bob is considered a value and is alawys true.
   print("Hello, " + name)  
else:
    print("Hello, stranger!") 

# Problem 10: y was equal to zero causing a ZeroDivisionError (undefined number)
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 5 # ZeroDivisionError 
print(divide_numbers(num1, num2)) 









