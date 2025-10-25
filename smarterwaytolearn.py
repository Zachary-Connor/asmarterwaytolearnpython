'''
Author: Zachary Connor

Last Updated: 10/24/2025

Program: Cover all 77 lessons and topics from Mark Myers' A Smarter Way to Learn Python
         I personally coded each lesson based on the topics covered, but they are quite
         similar to the book itself

Website: https://asmarterwaytolearn.com/python/index-of-exercises.html
'''
def main() -> None:

    # Lesson 1 - print function
    print("Lesson 1: ")
    print("Welcome to the smarterwaytolearn.py program!")

    # Lesson 2 - Variables for strings
    print("\nLesson 2: ")
    name = "Zach"
    print(name)

    # Lesson 3 - Variables for numbers
    print("\nLesson 3: ")
    num: int = 10
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
    number = int(input("Please enter your favorite number here: "))#convert number to an integer
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
    customer_29876: dict = {
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
    To loop through values in a dictionary, you must use the dictionary name followed by .values().
    This returns a view object of all of the values in the dictionary that you can then loop through
    using a traditional pythonic for loop
    '''
    print("\nLesson 31: ")
    print("Dictionary values: ")
    for value in customer_29876.values():
        print(value)
    # Lesson 32 - Dictionaries: Looping through keys
    '''
    Similar to looping through values in the above lesson, dictionaries also come with a function to iterate
    through the keys of a dictionary using the name followed by .keys()
    '''
    print("\nLesson 32: ")
    print("Dictionary keys: ")
    for key in customer_29876.keys():
        print(key)
    # Lesson 33 - Dictionaries: Looping through key-value pairs
    '''
    Dictionaries can be iterated through by using both a key and value pair with the items() function.
    Just like looping through values and keys, we use the dictionary name followed by .items(). The catch is that
    we need a second variable in the for loop.
    '''
    print("\nLesson 33: ")
    print("Here are the dictionary key and value pairs: ")
    for key, value in customer_29876.items():
        print(f"The key is {key} and the value is {value}")
    # Lesson 34 - Creating a list of Dictionaries
    '''
    Lists can hold dictionaries as well!
    '''
    print("\nLesson 34: ")
    customers = [
        {
            "customer_id": 1,
            "first name": "Zach",
            "last name": "Connor",
            "address": "12345 Dog Lane"
        },
        {
            "customer_id": 2,
            "first name": "Luffy",
            "last name": "Monkey",
            "address": "6789 Windmill Village"
        },
    ]
    print(customers)
    # Lesson 35 - How to pick information out of a list of dictionaries
    '''
    Since a list uses indexes, we just use the index to grab a dictionary out of the list or we can
    use another set of [] square brackets to access a key in the dictionary
    '''
    print("\nLesson 35: ")
    print(f"Here is the first name of customer 2 in the customers list: {customers[1]["first name"]}")
    # Lesson 36 - How to append a new dictionary to a list of dictionaries
    '''
    This process is just like appending any other item into a list
    '''
    print("\nLesson 36: ")
    new_dict: dict = {}
    new_customer_id: int = len(customers) + 1
    new_customer_fname: str = "Walter"
    new_customer_lname: str = "White"
    new_customer_address: str = "308 Negra Arroyo Lane."
    new_dict["customer id"] = new_customer_id
    new_dict["first name"] = new_customer_fname
    new_dict["last name"] = new_customer_lname
    new_dict["address"] = new_customer_address
    customers.append(new_dict)
    print(customers)
    # Lesson 37 - Creating a dictionary that contains lists
    '''
    The value in key-value pair can be a list of items in a dictionary. Dictionary keys however cannot be of the list type.
    '''
    print("\nLesson 37: ")
    dictionary_with_list: dict = {
        "list": [1, 2, 3],
    }
    print(f"Dictionary with a list: {dictionary_with_list}")
    # Lesson 38 - How to get information out of a list within a dictionary
    '''
    We can us the in key word to check if a list in a dictionary contains a specific element
    '''
    print("\nLesson 38: ")
    if 2 in dictionary_with_list["list"]:
        print("2 exists in the dictionary list!")
    else:
        print("2 does not exist in the dictionary list")
    # Lesson 39 - Creating a dictionary that contains a dictionary
    '''
    Dictionaries can be nested inside of each other. So a dictionary can have a key-value pair where the value is another dictionary with its own
    set of key-value pairs. How neat!
    '''
    print("\nLesson 39: ")
    nested_dict: dict = {
        0: {
            "name": "Zachary",
            "age": 22
        },
        1: {
            "name": "Gunther",
            "age": 25
        }
    }
    print(nested_dict)
    # Lesson 40 - How to get information out of a dictionary within another dictionary
    '''
    Remmber, in order to access a dictionary value we need the name of the key. Once we have the name of the key, we use the [] to access the value.
    Since there is a nested dictionary, we need the first key to the inner dictionary, and then we need to grab the second key which is the key that accesses
    the inner dictionaries key-value pairs to retrieve a value that mathces with the specified key. Essentially you will just use two sets of square brackets[][]
    to access the inner dictionary value.
    '''
    print("\nLesson 40: ")
    print(f"nested_dictionaries first inner dictionary name value is {nested_dict[0]["name"]}")
    # Lesson 41 - Functions
    '''
    Functions are used to modularize code and make it easy to repeat and reuse. Funtions use 
    the def keyword, the function name, and end with ():
    Anything inside the function must be indented properly. To invoke the functions, simply use
    its name followed by open and closed parenthesis
    '''
    print("\nLesson 41: ")

    def greet() -> None:
        print("Hello there from the greet function!")
    greet()
    # Lesson 42 - Functions: Passing them information
    '''
    Functions can receive information. The variables in the function definition are known as parameters,
    and the variables or values passed to the function call are known as arguments.
    '''
    print("\nLesson 42: ")
    def greet_name(name: str) -> None:
        print(f"Hello there {name}! ")
    greet_name("Gunther")

    # Lesson 43 - Functions: Passing information to them a different way
    '''
    We can pass values to specific parameters in the function call as long
    as the name of the parameter is known
    '''
    print("\nLesson 43: ")
    greet_name(name = "Zachary")
    # Lesson 44 -Functions: Assigning a default value to a parameter
    '''
    You can assign parameters a default value by using the assignment operator to assing them a value
    in the function definition. Note that if you have more than one parameter and one of the parameters
    does not contain a default value, it must be defined before all parameters with a default value.
    If the function is called without overriding parameters, default values are used instead
    '''
    print("\nLesson 44: ")
    def greet_john(name: str = "John") -> None:
        print(f"Hello {name}")
    greet_john()
    greet_john("Joey")

    # Lesson 45 - Functions: Mixing positional and keyword arguments
    '''
    When defining and calling functinos, it is important to know what keyword and posisitonal parameters and arguments are.
    Parameters are the variables used in the function definition, and arguments are the values or variables used in the function call.
    Positional parameters are parameters without keyword names, keyword parameters are named variables in the function definition.
    Posisitonal arguments follow the order of parameters defined in the function definition, and keyword arguments are specified in the function call.
    Keyword parameters and arguments always come last.
    '''
    print("\nLesson 45: ")
    def find_something(dct: dict = nested_dict, number: int = 0, key: str = "name") -> None:
        print(f"Inside dictionary, item number {number} has {key} as {dct[number][key]}")
    find_something()
    find_something(nested_dict, key = "age", number = 1)
    # Lesson 46 - Functions: Dealing with an unkown number of arguments
    '''
    When creating functions, we may want to have optional info we want to pass, but are not sure how many key-word parameters we need.
    We can get around this issue by using the double asterisk ** followed by a variable name which means there may or may 
    not be one or more extra arguments passed. The additional arguments are stored in a dictionary with the name of the
    ** variable used as a parameter. Optional arguments/parameters must come after regular arguments/parameters

    Posistional arguments can be optional as well. To handle optional positoinal arguments, you can use a single asterisk.
    The posisiotnal arguments beyond the ones specified in the definition are put into a tuple.
    '''
    print("\nLesson 46: ")
    # ** are used for an unkown number of key-word arguments stored in a dict
    def display_results(winner: str, score: str, **other_info) -> None:
        print(f"The winner was {winner}")
        print(f"The score was {score}")
        for key, value in other_info.items():
            print(f"{key}: {value}")

    display_results(winner = "Real Madrid", score = "1-0", overtime = True, injuries = "None")
    print()

    # * are used for an unkown number of positional arguments and stored in a tuple
    def display_nums(first_num, second_num, *opt_nums):
        print(first_num)
        print(second_num)
        print(opt_nums)
    
    display_nums(100, 200, 300, 400, 500)
    # Lesson 47 - Functions: Passing information back from them
    '''
    Functions can return information back to a function call, however they need a variable to store the return value.
    '''
    print("\nLesson 47: ")
    def what_is_my_name() -> str:
        return "Heisenberg"
    name: str = what_is_my_name()
    print(f"Say my name! You're {name}.")
    # Lesson 48 -Using functions as variables (which is what they really are)
    '''
    Function calls are replaced with the value that is returned by the function. This means you can use functions
    as parameters and variables in other areas of code
    '''
    print("\nLesson 48: ")
    print(f"Say my name! You're {what_is_my_name()}.")
    # Lesson 49 -Functions: Local vs. global variables
    '''
    To understand local vs global variables, we need to understand scope.
    Scope refers to what functions and other structures can access inside your code. It is what they can see and use.
    Local variables exist inside of functions, can can only be accessed by that function.
    Global variables exist outside of functions and can be accessed from anywhere.
    '''
    print("\nLesson 49: ")
    def print_y() -> None:
        #local variable y
        y: int = 12
        print(y)

    #global variable
    y: int = 1
    print_y()
    print(y)

    # Lesson 50 - Functions within functions
    '''
    As we have already seen, functions can be called inside of other functions, like when we use print
    in the above print_y() function
    '''
    print("\nLesson 50: ")
    print("Nothing new to add here")
    # Lesson 51 - While Loops
    '''
    While loops are similar to for loops, but they continue to loop as long as a condition is met.
    Once the condition is no longer met, the loop stops.
    '''
    print("\nLesson 51: ")
    x: int = 10
    while x > 0:
        print(x)
        x -= 1

    # Lesson 52 - While Loops Setting A Flag
    '''
    A flag is simply a boolean value, so True or False in Python. While loops typically use flags to control the number of iterations they do.
    '''
    print("\nLesson 52: ")
    flag: bool = True
    while flag:
        if x == 10:
            flag = False
        else:
            print(x)
            x += 1

    # Lesson 53 - Classes
    '''
    This is the heart of programming right here! Classes are templates that help us standardize and organize information.
    To create a class, we use the class keyword followed by the name of the class, and lastly parentheses with a colon ():.
    Ex: class Patient(): 
    Typically classes are Capitalized.
    '''
    print("\nLesson 53: ")
    print("We will create the class in the last class module which is 61")
    # Lesson 54 - Classes Starting to build the structure
    '''
    Since Classes represent objects, they need to be created somehow in the code.
    Classes have methods or functions known as constructors which are functions to initialize
    the class attributes. The constructor always uses the name __init__(self):
    Self refers to the class instance using the __init__() method. The constructor can have
    additonal paramters, but it must always include self.
    
    Building off of the Patient example, we get the following example:
    class Patient():
        def __init__(self, name):
    '''
    print("\nLesson 54: ")

    # Lesson 55 - Classes: A bit of housekeeping
    '''
    To properly give your class an attribute, it needs to further define a class instance variable in the constructor.
    Class attributes always start with self. in the class definition. Typically, you use the same name as the parameter.
    Here is our Patient example:
    class Patient():
        def __init__(self, last_name):
            self.last_name = last_name
    '''
    print("\nLesson 55: ")

    # Lesson 56 - Classes: Creating an instance
    '''
    To create an instance of our patient class, we need a variable and to call the class constructor.
    Ex: patient123 = Patient("Taleb")
    '''
    print("\nLesson 56: ")

    # Lesson 57 - Classes: A little more complexity
    '''
    Like I stated earlier, we can have Classes with more than one attribute
    Ex:
    class Patient():
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
    '''
    print("\nLesson 57: ")

    # Lesson 58 - Classes: Getting info out of instances
    '''
    We can directly access the Class attributes/members by using the instnace of the class, and the dot operator followed by the name of
    the Class attribute/member.
    Ex:
    pid123 = Patient("Gunther", "Bobby")
    print(pid123.first_name)
    '''
    print("\nLesson 58: ")

    # Lesson 59 - Classes: Building functions into them
    '''
    Classes can have functions built into them called methods. They too are treated like Class attributes/members
    and need to be called via the instance of the class, the dot operator, and the function name with the parentheses and
    function arguments if needed. EX:
    pid123.setAge(22)
    '''
    print("\nLesson 59: ")

    # Lesson 60 - Classes: Coding a method
    '''
    As stated above, Classes can have methods or functions built into them. All functions are created like regular functions
    except for the fact that their first parameter should always be the keyword self.
    EX:
    def setAge(self, newAge):
        self.age = newAge
    '''
    print("\nLesson 60: ")

    # Lesson 61 - Classes: Changing an attribute's value
    '''
    We can directly modify class instance attribute values by using the dot operator to access a specific member, and then we
    can use the assignment operator to assign the attribute a new value.
    Ex:
    pid123.age = 22
    '''
    print("\nLesson 61: ")
    class Student():
        def __init__(self, first_name: str, last_name: str, age: int) -> None:
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
        
        def __str__(self) -> str:
            return(f"first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}")
        
        def setAge(self, newAge: int) -> None:
            self.age = newAge

    pid123 = Student("Zachary", "Connor", 22)
    print(pid123)
    print(f"pid123.age = {pid123.age}")
    pid123.age = 23
    print(f"after age update, pid123.age = {pid123.age}")
    # Lesson 62 - Data files
    '''
    All of the output our code has generated has only gone to the terminal output. We can save information generated by our program in a file.
    To open a file in Python, we use the open keyword which is actually a built in function. The open function needs at least two parameters:
    a string representing the file name to open or create, and a letter such as w to write to the file, or do whatver like r for read, etc.
    Since open returns a file hanfle, we need a variable to store the file handle. EX: my_file = open("file.txt", "w").

    There is a key word with that we can use to close the file after we are done using it. It needs the open function as well as the "as" keyword
    to create the file handle and ends with a colon. Ex: with open("file.txt", "w") as file_to_work_with: 
    '''
    print("\nLesson 62: ")

    # Lesson 63 - Data Files: Storing Data 
    '''
    We can store information in files by writing to them. File processing uses the write command
    which is a function that is apart of the file handler create in the open statement. We pass the 
    function an argument which can be a string of text to put into the file. Ex:
    with open("patients.txt", "w") as file:
        file.write("Zach, Connor, 22)
    '''
    print("\nLesson 63: ")
    with open("patients.txt", "w") as file:
        file.write("Zach, Connor, 22")
    # Lesson 64 - Data Files: Retrieving Data
    '''
    We can also open files to read from them and use the data in our program. 
    By default, without specifying an option to open, it will read the file only.
    To read the entire file, you use the read() method from the file handler instance.
    Ex:
        with open("patients.txt", "r") as file:
            content: str= file.read()
    '''
    print("\nLesson 64: ")
    with open("patients.txt") as file:
        content: str = file.read()
    print(content)
    # Lesson 65 -  Data Files: Appending Data 
    '''
    In order to append data to a file instead of overwritting it, we use the option a instead of w.
    By default, append will add text to the same line, so we must add \n to write to different lines in the file.
    '''
    print("\nLesson 65: ")
    with open("patients.txt", "a") as file:
        file.write("\nGunther, Bobby, 1")

    with open("patients.txt") as file:
        print(file.read())
    # Lesson 66 - Modules
    '''
    This section talks about the fact that you can use other python files called modules in your main .py program.
    You use the import keyword and then the name of the file you want to include. For example,
    lets say you create a python file called calculations.py and you want to include it in another program.
    Inside that other program you use this line of code: import calculations
    You don't include the .py and to access any code from that file, you just specify it when calling functions.
    For example, lets say you want to use the calc() function from the imported file, you can just do
    calculations.calc(), and it will work!
    '''
    print("\nLesson 66: ")

    # Lesson 67 - CSV Files
    '''
    In order to read CSV files, we need access to the csv module. We do this by importing csv.
    Then we need to open the file the way we now know how to. Lastly, we use the reader function
    from csv to read the file by passing it the file handle.
    '''
    print("\nLesson 67: ")
    import csv
    with open("potions.csv") as file:
        content: str= csv.reader(file)
    print(content)
    # Lesson 68 - CSV Files: Reading them
    '''
    '''
    print("\nLesson 68: ")

    # Lesson 69 - CSV Files: Picking info out of them
    '''
    '''
    print("\nLesson 69: ")

    # Lesson 70 - CSV Files: Loading info into them part1
    '''
    '''
    print("\nLesson 70: ")

    # Lesson 71 - CSV Files: Loading info into them part2
    '''
    '''
    print("\nLesson 71: ")

    # Lesson 72 - CSV Files: Loading info into them part3
    '''
    '''
    print("\nLesson 72: ")

    # Lesson 73 - CSV Files: Appending rows to them
    '''
    '''
    print("\nLesson 73: ")

    # Lesson 74 - How to save a Python list or dictionary in a file: JSON
    '''
    '''
    print("\nLesson 74: ")

    # Lesson 75 - How to retrieve a Python list or dictionary from a JSON file
    '''
    '''
    print("\nLesson 75: ")

    # Lesson 76 - Planning for things to go wrong
    '''
    '''
    print("\nLesson 76: ")

    # Lesson 77 - A more practical example of exception handling
    '''
    '''
    print("\nLesson 77: ")

if __name__ == "__main__":
    main()