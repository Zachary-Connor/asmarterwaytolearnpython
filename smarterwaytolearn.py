'''
Author: Zachary Connor

Last Updated: 6/6/2025

Program: Cover all 77 lessons and topics from Mark Myers' A Smarter Way to Learn Python
         I personally coded each lesson based on the topics covered, but they are quite
         similar to the book itself

Website: https://asmarterwaytolearn.com/python/index-of-exercises.html
'''

# Lesson 1 - print function
print("Lesson 1: ")
print("Welcome to the smarterwaytolearn.py program!")

# Lesson 2 - Variables for strings
print("\nLesson 2: ")
name = "Zach"
print(name)

# Lesson 3 - Variables for numbers
print("\nLesson 3: ")
num = 10
print(num)

# Lesson 4 - Math expressions: familiar operators
print("\nLesson 4: ")
num1 = 10
num2 = 20
total = num1 + num2
print(str(num1) + " + " + str(num2) + " = " + str(total))
total = num1 - num2
print(str(num1) + " - " + str(num2) + " = " + str(total))
total = num1 * num2
print(str(num1) + " * " + str(num2) + " = " + str(total))
total = num1 / num2
print(str(num1) + " / " + str(num2) + " = " + str(total))

# Lesson 5 - Variable Names Legal and Illegal 
'''
Variable names can only contain alphanumeric symbols and underscores, no special symbols.
Variable names cannot start with a number either. Keywords cannot be used as variable names.
'''

# Lesson 6 - Math Expressions: Unfamiliar operators
'''
The unfamiliar operators are:
modulo % which finds the remainder between two integers
+= to increment the left hand side by the right hand side. EX: num = 10, num += 1. num is now 11
-= to decrement the left hand side by the right hand side. EX: num = 10, num -= 1. num is now 9
*= to multiply the left hand side by the right hand side. EX: num = 10, num *= 2. num is now 20
'''
print("\nLesson 6: ")
num1 = 10
num2 = 3
total = num1 % num2
print(str(num1) + " % " + str(num2) + " = " + str(total))
total += 1
print("total = 1\ntotal += 1\ntotal = " + str(total))

# Lesson 7 - Math expressions: Eliminating ambiguity
'''
Consider the algebraic statement total = 1 + 3 * 4. What is the result? is it 16 or 13.
Python, similar to algebra, follows the order of precedence or PEMDAS from school.
It will do multiplication or division or modulo first, then it will do addition or subtraction.
The statements are read from left to right which is the associativity of the operator/equation.
Parentheses override the order of precedence allowing you to specify the order of operations as needed.
'''
print("\nLesson 7: ")
num1 = 1
num2 = 3
num3 = 4
total = 1 + 3 * 4
print(str(num1) + " + " + str(num2) + " * " + str(num3) + " = " + str(total))
total = (1 + 3) * 4
print("(" + str(num1) + " + " + str(num2) + ") * " + str(num3) + " = " + str(total))
total = 1 + (3 * 4)
print(str(num1) + " + (" + str(num2) + " * " + str(num3) + ") = " + str(total))

# Lesson 8 - Concatenating text strings
'''
In python, we can "add" text strings together which is known as concatenation
we can create a string variable to store many words added together via other strings or variables
Be mindful of the data the variable holds as you can't combine text strings with integers or numbers
The print function can also accept the plus sign to concatenate strings together
Note that you can only add numbers with other numbers and strings with other strings
You cannot add a number and string together
'''
print("\nLesson 8: ")
greeting = "Hello"
separators = ", "
addressee = "World"
punc = "!"
whole_greeting = greeting + separators + addressee + punc
print(whole_greeting)
print("Hello," + " World!")
print(greeting + separators + addressee + punc)

# Lesson 9 - if statements
'''
if statements are used to represent logic in programs. They can handle many expressions to form conditions which are evaluated to true or false.
if statements will only be executed if the expression it contains is true.
In python, we use indentation to create blocks of code, so anything indented below a colon is apart of that block of code
'''
print("\nLesson 9: ")
num = 12
if num == 12:
    print("num is equal to 12")
print("All done!") # since this line is not indented it will always be executed regardless of the condition

# Lesson 10 - Comparison operators
'''
There are many logic or boolean operators that are used for comparison: <, >, <=, >=, ==, !=
'''
print("\nLesson 10: ")
if num <= 100:
    print("num is less than 100")
# Lesson 11 - else and elif statement
'''
We can add additional statements that test further conditions and expressions when the initial if statement does not evaluate to true
These statements are elif and else.
elif stands for else if and it expects new criteria to be met
else is a catchall and only one else statement is needed in a block of conditional statements
When an if or elif are evaluated as true, all other elif and else statements below it are ignored.
'''
print("\nLesson 11: ")
if num == 0:
    print("num is zero")
elif num % 2 == 0:
    print("num is even")
else:
    print("num is odd")

# Lesson 12 - Testing sets of conditions
'''
We can combine multiple conditons in one if statement. This allows for more complex logic
The two keywords that help us here are: and, or.
and requires that both conditions must be true to be evaluated as true
or requires only 1 condition to be true to be evaluated as true
These conditional keywords also have an order of precedence, so use parentheses to make it more readable.
and has a higher precedence than or, so be aware of this if parentheses are not used.
'''
print("\nLesson 12: ")
if num == 12 and num1 != 12:
    print("num is 12, and num1 is not 12")
else:
    print("failed")
# Lesson 13 - if statements nested
'''
We can place more conditional statements that are nested (indented) inside of other conditional statements.
This is harder to read, so try to use the two keywords: and, or.
Although certain scenarios require nested structures, so use them as needed
'''
print("\nLesson 13: ")
if num % 2 == 0:
    if num == 12:
        print("num is 12")
    elif num == 4:
        print("num is 4")
    else:
        print("num is even")
else:
    print("num is odd")

# Lesson 14 - Comments
'''
Comments are used to add description of code for humans to read. The machine ignores the characters inbetween these symbols
Single Line Comments are made using the # symbol
Multi Line Comments are made using the ' symbol three times with no whitespaces inbetween them (This is what I am using write these comments)
'''
print("\nLesson 14: ")
print("# are used for single line comments and ''' is used for mutlti line comments")
# Lesson 15 - Lists
'''
In python there are built in data structures. We have been working with integers, floats, and strings.
The first data structure we cover is called a list.
We can think of this like a grocery list. We have multiple items in the list.
Lists store values using indexes which is a number assigned to each list element to grab the information at the specified index.
List indexes always start at 0 and go in ascending order
Ex: we have a list of 3 numbers: nums = [1, 2, 3]. To access the first number, we say nums[0].
Lists are indicated using the [] symbols and each element in the list is separated by a comma.
'''
print("\nLesson 15: ")
hobbies = ["Working Out", "Listening to Music", "Walking my dog", "Video games", "Coding", "Watching Shows"]
print("hobbies[0] = " + hobbies[0])
# Lesson 16 - Lists: Adding and changing elements
'''
Lists are mutable in Python. This means we can change and modify the structure of the list, so its contents can change.
There are a couple ways we can add elements to the list: append, attach another list, insert, subscript operator with index [num].
Append: my_ist.append(value) - this will add value at the end of the list my_list
Adding another list: my_list = my_list + [value1, value2] - adds the list containing value1 and value2 at the end of the list
Insert: my_list.insert(0, value) - inserts value at the beginning of the list (insert always requires an index when calling the function)
Array subscript operator []: my_list[0] = value - modifies the element at index 0 to be value
'''
print("\nLesson 16: ")
print("hobbies before changes: ", end = "")
print(hobbies)
hobbies.append("Cooking")
hobbies = hobbies + ["Running", "Reading"]
hobbies[0] = "Exercise"
print("hobbies after changes: ", end = "")
print(hobbies)
# Lesson 17 - Lists: Taking slices out of them (Challenging at first)
'''
We can take slices or chunks out of a list and do many things with it like creating other lists.
To take a list slice we do the following: new_list = my_list[x:y].
X represents the beginning index, and y represents the ending index.
The beginning index starts at the location specified
The ending index stops 1 index before the integer value.
For example, list[0:4] grabs the elements from indexes 0 to 3.
If the slice starts at index 0, it can be omitted. Ex: list[:4]
If the slice ends on the last element, it can be omitted. Ex: list[4:]
'''
print("\nLesson 17: ")
slice1 = hobbies[1:4]
print("slice1 = hobbies[1:4]: ", end ="")
print(slice1)
slice2 = hobbies[:4]
print("slice2 = hobbies[:4]: ", end ="")
print(slice2)
slice3 = hobbies[4:]
print("slice3 = hobbies[4:]: ", end ="")
print(slice3)
# Lesson 18 - Lists: Deleting and removing elements
'''
We can delete and remove elements from Lists in Python, and yes there is a difference.
Deleting uses the keyword deland requires the list index to delete the item. Keep in mind after deleting an element from a list,
the list indexes are updated to account for the deleted element.
EX: del my_list[0] - removes the first element from the list and updates the remaining indexes

Removing uses the remove method and requires the elements value instead of its index. It also updates the indexes of the remaining list elements
EX: my_list.remove(value)
'''
print("\nLesson 18: ")
print("hobbies list before deletes and removes: ", end = "")
print(hobbies)
del hobbies[0]
del hobbies[2]
hobbies.remove("Listening to Music")
print("hobbies list after deletes and removes: ", end = "")
print(hobbies)
# Lesson 19 - Lists: popping elements
'''
Pop is different than the delete or remove functions as pop will return the value that is being removed.
Pop requires the index of the element to be removed, and if no value is passed, it will remove the last element in the list
EX: number = my_list.pop(0) - removes the first element from my_list and stores the value in the variable number
EX: number = my_list.pop() - removes the last element from my_list and stores the value in the variable number
'''
print("\nLesson 19: ")
print("hobbies list before popping: ", end = "")
print(hobbies)
favorite_hobby = hobbies.pop()
print("My favorite hobby is: " + favorite_hobby)
print("hobbies list after popping: ", end = "")
print(hobbies)
# Lesson 20 - Tuples
'''
Tuples are very similar to lists except for the fact that they cannot be changed. This is called immutable
Tuples are denoted by () parenthesis and cannot be modified. To modify a tuple, you must redefine it entirely
Tuples are accessed by indexes just like lists are
'''
print("\nLesson 20: ")
nums = (1, 2, 3, 4)
print(f"nums[1] = {nums[1]}")
print(f"combine first two numbers in tuple = {nums[0] + nums[1]}")
# Lesson 21 - for loops
'''
For loops are used to iterate through objects or ranges of numbers to repeat a task or grab the next item
They end with a : and anything inside the loop is indented. You can place more structures like if statements inside of them
'''
print("\nLesson 21: ")
saints = ["Padre Pio", "Augustine", "Francis of Assisi"]
for a_saint in saints:
    if a_saint is "Padre Pio":
        print(f"{a_saint} - Shia LeBeouf acted as him!")
    else:
        print(f"{a_saint} - Shia LeBeouf did not act as him.")
# Lesson 22 - for loops nested
'''
We can nest for loops to go through 2 dimensinoal structures. There is an outer loop and an inner loop.
The outer loop starts the first iteration and then goes down into the inner loop while the inner loop controls an entire cycle
before returning to the outer loop for the next iteration
'''
print("\nLesson 22: ")
vowels = ("a", "e", "i", "o", "u")
word = "Hello"
for a_letter in word:
    for a_vowel in vowels:
        if a_letter == a_vowel:
            print(f"found a vowel in {word}: {a_vowel}")

# Lesson 23 - Getting information from the user and converting strings and numbers
'''
Getting input from the user is quite straight forward in Python. simply use the input() function to grab input
You need to store the input into a variable and all values grabbed from input are strings by default.
To change the data type of the variable you can enclose them in other functions like int(), str(), float(), bool(), etc.
You can prompt the user by adding string text inside the input() function.
'''
print("\nLesson 23: ")
number = input("Please enter your favorite number here: ") #number is a string currently
number = int(number) # convert number to be an integer instead of a string
number += 10
print("Here is your number plus 10: " + str(number))
# Lesson 24 - Changing case
'''
This lesson covers three main functions: lower(), upper(), and title()
lower() converts the string into all lowercase letters
upper() converts the string into all uppercase letters
title() converts the string to start all words with an uppercase letter and the remaining letters to be lowercase
'''
print("\nLesson 24: ")
city = input("Please enter the city you were born in: ")
print(f"You were born in {city}")
print(f"You were born in {city.lower()}")
print(f"You were born in {city.upper()}")
print(f"You were born in {city.title()}")
# Lesson 25 - Dictionaries: What they are
'''
Dictionaries are a built in data structure for python. Instead of using indexes like lists and tuples,
Dictionaries use key value pairs typically to represent objects and their attributes.
For example lets say we want to know the information of cutomer 6789's order.
The have a first name field and a value associated with it, a last name field and a value associated with it, etc
'''
print("\nLesson 25: ")
print("This lesson was used as review for other subjects. Simply refer to previous lessons.")
# Lesson 26 - Dictionaries: How to code one
'''
Dictionaries are enclose in {} curly brackets and the left hand side of a : colon is the key and the right hand side
of the : colon is the value. Each key value pair is separated by a comma. Both keys and values can be different data types, but in this
example I will use strings for both key and value in the dictionary
'''
print("\nLesson 26: ")
customer_29876 = {
    "first name": "David",
    "last name": "Elliot",
    "address": "4803 Wellesley St."
}
print(customer_29876)
# Lesson 27 - Dictionaries: How to pick information out of them
'''
In order to grab information from a dictionary, we need to know each elements key. We use the [] square brackets like we
would with a list, except intead of using an index value, we use the key to extract its values
'''
print("\nLesson 27: ")
print(f"The customer's last name is {customer_29876["last name"]}")
# Lesson 28 - Dictionaries: The versatility of keys and values
'''
Keys and values can be of different data types like strings and numbers
'''
print("\nLesson 28: ")
print("No new code here")
# Lesson 29 - Dictionaries: Adding items
'''
To add an item to a dictionary, all you need to do is specify the dictionary name and the key on the
left side of the = and on the right side the value.
'''
print("\nLesson 29: ")
print(f"customer_29876 before: {customer_29876}")
customer_29876["city"] = "Toronto"
print(f"customer_29876 after: {customer_29876}")
# Lesson 30 - Dictionaries: Removing and changing items
'''
To remove an item from a dictionary, it is similar to removing an element from a list using its index.
Simply use the keyword del, the name of the dictionary, and the key to remove it from the dictionary.
You can also overwrite data in a dictionary by reassigning the key a different value
'''
print("\nLesson 30: ")
print(f"customer_29876 before: {customer_29876}")
del customer_29876["city"]
customer_29876["last name"] = "Connor"
print(f"customer_29876 after: {customer_29876}")
# Lesson 31 - Dictionaries: Looping through values
'''
'''
print("\nLesson 31: ")
# Lesson 32 - Dictionaries: Looping through keys
'''
'''
print("\nLesson 32: ")
# Lesson 33 - Dictionaries: Looping through key-value pairs
'''
'''
print("\nLesson 33: ")
# Lesson 34 - Creating a list of Dictionaries
'''
'''
print("\nLesson 34: ")
# Lesson 35 - How to pick information out of a list of dictionaries
'''
'''
print("\nLesson 35: ")
# Lesson 36 - How to append a new dictionary to a list of dictionaries
'''
'''
print("\nLesson 36: ")
# Lesson 37 - Creating a dictionary that contains lists
'''
'''
print("\nLesson 37: ")
# Lesson 38 - How to get information out of a list within a dictionary
'''
'''
print("\nLesson 38: ")
# Lesson 39 - Creating a dictionary that contains a dictionary
'''
'''
print("\nLesson 39: ")
# Lesson 40 - How to get information out of a dictionary within another dictionary
'''
'''
print("\nLesson 40: ")
# Lesson 41 - Functions
'''
'''
print("\nLesson 41: ")
# Lesson 42 - Functions: Passing them information
'''
'''
print("\nLesson 42: ")
# Lesson 43 - Functions: Passing information to them a different way
'''
'''
print("\nLesson 43: ")
# Lesson 44 -Functions: Assigning a default value to a parameter
'''
'''
print("\nLesson 44: ")
# Lesson 45 - Functions: Mixing positional and keyword arguments
'''
'''
print("\nLesson 45: ")
# Lesson 46 - Functions: Dealing with an unkown number of arguments
'''
'''
print("\nLesson 46: ")
# Lesson 47 - Functions: Passing information back from them
'''
'''
print("\nLesson 47: ")
# Lesson 48 -Using functions as variables (which is what they really are)
'''
'''
print("\nLesson 48: ")
# Lesson 49 -Functions: Local vs. global variables
'''
'''
print("\nLesson 49: ")
# Lesson 50 - Functions within functions
'''
'''
print("\nLesson 50: ")

# Lesson 51 - 
'''
'''
print("\nLesson 51: ")

# Lesson 52 - 
'''
'''
print("\nLesson 52: ")

# Lesson 53 - 
'''
'''
print("\nLesson 53: ")

# Lesson 54 - 
'''
'''
print("\nLesson 54: ")

# Lesson 55 - 
'''
'''
print("\nLesson 55: ")

# Lesson 56 - 
'''
'''
print("\nLesson 56: ")

# Lesson 57 - 
'''
'''
print("\nLesson 57: ")

# Lesson 58 - 
'''
'''
print("\nLesson 58: ")

# Lesson 59 - 
'''
'''
print("\nLesson 59: ")

# Lesson 60 - 
'''
'''
print("\nLesson 60: ")

# Lesson 61 - 
'''
'''
print("\nLesson 61: ")

# Lesson 62 - 
'''
'''
print("\nLesson 62: ")

# Lesson 63 - 
'''
'''
print("\nLesson 63: ")

# Lesson 64 - 
'''
'''
print("\nLesson 64: ")

# Lesson 65 - 
'''
'''
print("\nLesson 65: ")

# Lesson 66 - 
'''
'''
print("\nLesson 66: ")

# Lesson 67 - 
'''
'''
print("\nLesson 67: ")

# Lesson 68 - 
'''
'''
print("\nLesson 68: ")

# Lesson 69 - 
'''
'''
print("\nLesson 69: ")

# Lesson 70 - 
'''
'''
print("\nLesson 70: ")

# Lesson 71 - 
'''
'''
print("\nLesson 71: ")

# Lesson 72 - 
'''
'''
print("\nLesson 72: ")

# Lesson 73 - 
'''
'''
print("\nLesson 73: ")

# Lesson 74 - 
'''
'''
print("\nLesson 74: ")

# Lesson 75 - 
'''
'''
print("\nLesson 75: ")

# Lesson 76 - 
'''
'''
print("\nLesson 76: ")

# Lesson 77 - 
'''
'''
print("\nLesson 77: ")

