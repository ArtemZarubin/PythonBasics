import datetime as dt  # Standard modules in python
import os
import random
import sys
import time
import platform
import cowsay
import webbrowser

import my_module  # My own module

from math import sqrt

print("My company name is Devult")  # Name of my company
# first comment
print("Number:", 7620, "and number:", 1337)  # Favorite number 7620, and 1337 is streaming
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Output without any useless space: ", 76201373, " and very cool company name is ", 934717, sep="")  # Just
# output
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Example where I don't use \'Enter\'", sep="", end=". ")  # Parameters
print("See? Without any \'Enter\'")
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Using quote mark like this \"\"\"")  # End symbols
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Simple mathematics: 7620/1373 = ", 7620 / 1337, sep="")  # Math
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Squaring number 7^2: ", 7 ** 2, sep="")  # Squaring
print("Division without remainder: ", 7 // 2, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Minimum number of this: 7620, 1337, 18, 16 = ", min(7620, 1337, 18, 16), sep="")  # Min and max functions
print("Maximum number of this: 7620, 1337, 18, 16 = ", max(7620, 1337, 18, 16), sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Squaring number 7^2, but with function \'pow\' ", pow(7, 2), sep="")  # Squaring in another way
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Round number to closest (7620 / 1337): ", round(7620 / 1337), sep="")  # Round number
print()

# ---------------------------------------------------------------------------------------------------------------------
input("Enter something: ")  # First use of input, enter anything
print()

# ---------------------------------------------------------------------------------------------------------------------
fav_number = 7620  # Create a variable
print("My favorite number: ", fav_number, sep="")  # Show variable
del fav_number  # Deleting my variable
print()

# ---------------------------------------------------------------------------------------------------------------------
user_name = input("Enter your name: ")  # Enter a name
print("Hello, ", user_name, "!", sep="")  # Show the name
print()
# ---------------------------------------------------------------------------------------------------------------------
pi = 3.14159265358979
print("Number pi = ", pi, sep="")
print()
# ---------------------------------------------------------------------------------------------------------------------
company_name = "Devult"
print("Best company in the world is ", company_name, sep="")
print()
# ---------------------------------------------------------------------------------------------------------------------
say_truth = True
print("Are you telling me the truth? And = ", say_truth, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
any_number = 1337
any_string = "Twitch = "
print("Cast to string: ", any_string + str(any_number), sep="")

normal_number = 1337
normal_string = "7620"
print("Cast to number: ", normal_number + int(normal_string), sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
result_of_plus = first_number + second_number
print("Sum of your numbers ", first_number, " and ", second_number, " = ", result_of_plus, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
multiple_string = "Halo! "
print(multiple_string * 5, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
check_age = int(input("Enter your age: "))
if check_age >= 10:
    if check_age >= 14:
        if check_age >= 18:
            if check_age >= 60:
                print("You are an old!")
            else:
                print("You are an adult!")
        else:
            print("You are a teenager!")
    else:
        print("You are a kid!")
else:
    print("You are too young!")
print()

# ---------------------------------------------------------------------------------------------------------------------
are_you_happy = bool(input("Write \'True\' for happiness and \'False\' for bad day: "))
if not are_you_happy:
    print("Get better bro!")
else:
    print("It's cool that you have great day!")
print()

# ---------------------------------------------------------------------------------------------------------------------
enter_0_or_1 = int(input("Enter 0 or 1: "))
if enter_0_or_1 == 0:
    print("Number is 0!")
elif enter_0_or_1 == 1:
    print("Number is 1")
else:
    print("I have no idea what number is that!")
print()

# ---------------------------------------------------------------------------------------------------------------------
favorite_number = int(input("Enter my favorite number = "))
streaming_number = int(input("Enter a streaming number = "))
if (favorite_number == 7620) and (streaming_number == 1337):
    print("Good afternoon, ms. Zarubin-Artem!")
else:
    print("Sorry, but you are not Artem Zarubin!")
print()

# ---------------------------------------------------------------------------------------------------------------------
users_data = str(input("Enter your name: "))
name_of_user = "Hello, " + users_data + "!" if users_data == "Artem" else "Sorry, you are not Artem!"
print(name_of_user)
print()

# ---------------------------------------------------------------------------------------------------------------------
for i in range(0, 26, 5):  # Using loop for first time
    print("Number: ", i, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
word = "Devult"  # Fav company
for i in range(len(word)):
    print(i)
print()

# ---------------------------------------------------------------------------------------------------------------------
check_word = str(input("Enter any sentence: "))  # find letter program
count_letters = 0
for i in check_word:
    if i == "o":
        count_letters += 1
print("I have found ", count_letters, " letters \'o\' in your sentence:", check_word)
print()

# ---------------------------------------------------------------------------------------------------------------------
loop_counter = 0  # Loop while
while loop_counter < 10:
    print("Your number is ", loop_counter)
    loop_counter += 1
print()

# ---------------------------------------------------------------------------------------------------------------------
word_stop_for_end = True  # Say stop to stop program
while word_stop_for_end:
    if str(input("Enter any word, if you want to stop, write \'stop\': ")) == "stop":
        word_stop_for_end = False
print()

# ---------------------------------------------------------------------------------------------------------------------
for i in range(0, 20):  # Break and continue
    if i == 11:
        break
    if (i % 2) == 1:
        continue
    print("Our number is ", i, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
enter_word = str(input("Enter any word: "))  # Modernized program to find a letter
check_letter = None
for i in enter_word:
    if i == "o":
        check_letter = True
        break
    else:
        check_letter = False
if check_letter:
    print("I have found \'o\' in your sentence!")
else:
    print("Sorry, I haven't found \'o\' in your sentence!")
print()

# ---------------------------------------------------------------------------------------------------------------------
array_of_nums = [7, 6, 2, 0, 1, 3, 3, 7, "Devult", 3.14159265358979, True]  # All types in one list
print("Showing array: ", array_of_nums, sep="")
array_of_nums[3] = 'O'
print("Showing modified array: ", array_of_nums, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
adding_nums = [7, 6, 2, 0]  # Funny methods with list
add_num = int(input("Enter any number to add in the end of a list: "))
adding_nums.append(add_num)
print("Our list with added number = ", adding_nums, sep="")
print()

add_num_in_middle = int(input("Enter any number to add in the middle of the list: "))
adding_nums.insert(3, add_num_in_middle)
print("Our list with added number = ", adding_nums, sep="")
print()

adding_nums.sort()
print("Sorted list: ", adding_nums, sep="")
print()

adding_nums.reverse()
print("Reversed sorted list: ", adding_nums, sep="")
print()

adding_nums.pop()
print("Deleting last number from list: ", adding_nums, sep="")
print()

adding_nums.remove(2)
print("Remove number 2 from list: ", adding_nums, sep="")
print()

adding_nums.pop(2)
print("Deleting 2nd number from list: ", adding_nums, sep="")
print()

print("Numbers in list: ", len(adding_nums), sep="")
print()
print()

# ---------------------------------------------------------------------------------------------------------------------
normal_list = [1, 3, 3, 7, " | ", 7, 6, 2, 0]  # Showing list in normal way
for i in normal_list:
    print(i, end="")
print()

# ---------------------------------------------------------------------------------------------------------------------
users_list_range = int(input("Enter range of a list: "))  # First usage of normal list
zero_num = 0
users_list = []
while zero_num < users_list_range:
    users_list.append(input("Enter element: "))
    zero_num += 1
print("Your list:")
for i in users_list:
    print(i, end=" ")
print()

# ---------------------------------------------------------------------------------------------------------------------
rand_list = []  # List full of random numbers
enter_diapason = int(input("Enter how much number generate: "))
for i in range(enter_diapason):
    random_num = random.randint(1, 100)
    rand_list.append(random_num)

print("List full of random:")
for i in rand_list:
    print(i, end=" ")
print()
print()
# ---------------------------------------------------------------------------------------------------------------------
small_word = 'all words here in upper or capitalize case'  # Funny methods with strings
print("Example of sentence: ", small_word, ". Making your sentence in upper case: ", small_word.upper(), sep="")
small_word.lower()
print("Now every first letter of the word in capitalize case: ", small_word.capitalize(), sep="")
print()

spliting_word = "cycling, programming, youtube"
store_split = spliting_word.split(', ')
print("Spliting line: ", spliting_word, " to = ", spliting_word.split(', '))
print("Second element of list is \'", store_split[1], "\'", sep="")

print("Capitalazing every word:", end=" ")
for i in range(len(store_split)):
    store_split[i] = store_split[i].capitalize()
    print(store_split[i], " ", sep="", end=" ")
print()
print()

result_of_split = ", ".join(store_split)
print("Now it's a line and not a list: ", result_of_split, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
word_cut = "Cut me dude!"  # Cutting everything
funny_cutting = "It's just a simple sentence to cut it somehow you want to! >:=)"
print("I cut line \'", word_cut, "\' to = ", word_cut[0:6])
print("Cut line \'", funny_cutting, "\' to = ", funny_cutting[0::2])
print()

line_of_funny_things = ["Stream-sniping", 1337, "rizz", "Ivi", 7620, "Devult"]
print("Cutting the whole list: ", line_of_funny_things[2:])

print("Reversing whole list only with print = ", line_of_funny_things[::-1])
print()

# ---------------------------------------------------------------------------------------------------------------------
first_time_tuple = (7620, "Devult", 1337, "Valorant", "Devult", "Devult", "Devult")  # It's a tuple and not a list.
# It's like constant list

print("Second element of tuple is \'", first_time_tuple[1], "\'", sep="")
print("How much \'Devult\' words in tuple = ", first_time_tuple.count("Devult"), sep="")
print("There is ", len(first_time_tuple), " elements in the tuple = ", first_time_tuple, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
tuple_without_braces = 5, "GG", "val", "exe", "war", 76, 93  # Tuple but without brackets
print("Printing tuple without any braces in initialization: ", tuple_without_braces, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
creating_tuple_out_of_list = ["Something", 411, "USA", 'Seattle', True, 90210]  # List to tuple
print("It's list = ", creating_tuple_out_of_list, sep="")
tuple_of_list = tuple(creating_tuple_out_of_list)
print("But now it's a tuple = ", tuple_of_list, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
letter_tuple = "Best company is Devult!"  # Tupling sentence
print("Tupling a sentence = ", tuple(letter_tuple), sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
country_Ukraine = {'code': "UA", 'name': "Ukraine", 'population': 43000000, 'status': "War"}  # Dictionary
print("Showing dict of Ukraine. Population is ", country_Ukraine['population'], sep="")
country_USA = dict(code="USA", name="United States of America", population=3310000000, status="Best")  # Another way
print("Showing dict of USA in another way. Status is ", country_USA['status'], sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
country_Russia = {'code': "RU", 'name': "Russia", 'population': 144000000, 'status': "War"}  # Showing full info
for key, val in country_Russia.items():
    print(key, " - ", val, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
print("Using \'get\' = ", country_Russia.get('code'), sep="")  # Getting key and clearing
country_Russia.clear()  # Clearing full dictionary
print()

# ---------------------------------------------------------------------------------------------------------------------
country_Ukraine.pop('population')  # Showing everything
print("I have popped element \'population\' out of Ukraine = ", country_Ukraine, sep="")
print("All keys of USA = ", country_USA.keys(), sep="")
print("All values of USA = ", country_USA.values(), sep="")
print("All about USA = ", country_USA.items(), sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
country_USA['code'] = "US"  # Updating value
country_USA.update(religion="catholic")
print("Updated dictionary of USA = ", country_USA, sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
person = {  # Creating small data base
    'Artem': {
        'name': "Artem",
        'age': 18,
        'status': "Unemployed",
        'education': "University",
        'favorite color': "yellow",
        'address': ('Georgia', 'Batumi', 'Lermontova', '67')
    },
    'Maksim': {
        'name': "Maksim",
        'age': 18,
        'status': "Employed",
        'education': "University",
        'favorite color': "black",
        'address': ('Poland', 'Warshawa', 'Lomonosova', '34')
    },
    'MK': {
        'name': "Maksim",
        'age': 18,
        'status': "Unemployed",
        'education': "University",
        'favorite color': "purple",
        'address': ('Russia', 'Tokmak', 'Griboedova', '24')
    }
}
print("Info about ", person['Artem']['name'], ", address = ", person['Artem']['address'], " = ", person['Artem'],
      sep="")
print("Info about ", person['Maksim']['name'], ", address = ", person['Maksim']['address'], " = ", person['Maksim'],
      sep="")
print("Info about ", person['MK']['name'], ", address = ", person['MK']['address'], " = ", person['MK'], sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
data = set('hello dude')  # Using set for first time
print(data)

data_set = {"Programming", "Music", "Cycling", "Sudoku", "Meditation", "Music", "Davin-chi"}
print("Showing set with deleted elements = ", data_set)

data_set.add("Best Friend")
data_set.update(["Devult"])
data_set.remove("Meditation")
print("Updated set = ", data_set)

data_set.clear()  # Clearing set
print()

# ---------------------------------------------------------------------------------------------------------------------
enter_set = int(input("Enter number of your hobbies: "))  # Using set for users input
users_set = []
data_users_set = {}
for i in range(enter_set):
    users_set.append(str(input("Enter hobby: ")))
print("Your hobbies = ", users_set)

data_users_set = set(users_set)
print("Sorting and updating your list of hobbies = ", data_users_set)
print()

# ---------------------------------------------------------------------------------------------------------------------
real_name = str(input("Enter your real name: "))  # Frozenset for users data
real_surname = str(input("Enter your real surname: "))
full_data_about_user = frozenset([real_name, real_surname])
print("Data about user what you can't change = ", full_data_about_user)
print()


# ---------------------------------------------------------------------------------------------------------------------
def show_message(counter):  # Creating my first function which just show a message
    for time_show in range(counter):
        print("Everlong!!!")


abusing_func = int(input("Enter how much time you want to use function: "))
show_message(abusing_func)
print()


# ---------------------------------------------------------------------------------------------------------------------
def summa(first_number_sum, second_number_sum):  # Function which counts sum of 2 numbers
    return first_number_sum + second_number_sum


write_first = int(input("Enter first number for plus: "))
write_second = int(input("Enter second number for plus: "))
result_of_plusing = summa(write_first, write_second)
print("Sum of your numbers = ", result_of_plusing, sep="")
print()


# ---------------------------------------------------------------------------------------------------------------------
def find_min(first_min, second_min):  # Finding, minimum in 2 numbers
    if first_min > second_min:
        return second_min
    else:
        return first_min


def find_max(first_max, second_max):  # Finding maximum in 2 numbers
    if first_max > second_max:
        return first_max
    else:
        return second_max


using_min_max_first = int(input("Enter first any number to find min and max = "))
using_min_max_second = int(input("Enter second any number to find min and max = "))
print("Min of ", using_min_max_first, " and ", using_min_max_second, " is \'",
      find_min(using_min_max_first, using_min_max_second), "\'", sep="")
print("Max of ", using_min_max_first, " and ", using_min_max_second, " is \'",
      find_max(using_min_max_first, using_min_max_second), "\'", sep="")
print()


# ---------------------------------------------------------------------------------------------------------------------
def find_min(any_list=None):  # Finding minimum in list of numbers
    if any_list is None:
        any_list = []
    min_number = any_list[0]
    for element_count in any_list:
        if min_number > element_count:
            min_number = element_count
    return min_number


min_list = [54, 1243, -23, 7620, -1337, 1337, 18, 76, -452, 12, 3214, -124, 123, 457, 657, -412445, 14, -5132]
print("Minimal element in list is ", find_min(min_list), sep="")
print()

# ---------------------------------------------------------------------------------------------------------------------
starting_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                 20]  # Using lambda for first time to filter list
create_new_list = list(filter(lambda element: (element % 2 == 0), starting_list))
print("Old list = ", starting_list)
print("Creating new list with lambda's help = ", create_new_list)
print()


# ---------------------------------------------------------------------------------------------------------------------
def create_list(amount_of_elements):  # Function created only by me to create new list with random numbers
    creating_new_list = []
    for element in range(amount_of_elements):
        randomized_num = random.randint(1337, 7620)
        creating_new_list.append(randomized_num)
    return creating_new_list


enter_num_of_elements = int(input("Enter amount of elements in list: "))
equal_to_list = create_list(enter_num_of_elements)
print("Our new brand list made out of random numbers = ", equal_to_list)
print()

# ---------------------------------------------------------------------------------------------------------------------
first_file = open('Devult Data/Devult.txt', 'w')  # Using files for first time

first_file.write("Devult company is the best company ever!\n")
first_file.write("This company was created by Artem Zarubin! With help of his friend MK and MMM!\n")

data_put = str(input("Enter any text to append it in file: "))
first_file.write(data_put + "\n")

first_file.close()
print()

# ---------------------------------------------------------------------------------------------------------------------
editing_file = open('Devult Data/Devult.txt', 'r')  # Reading file for first time
print(editing_file.read())
editing_file.close()

# ---------------------------------------------------------------------------------------------------------------------
with open('Devult Data/Devult.txt', 'a',
          encoding="utf-8") as file_write:  # Using open file better like this and append data
    file_write.write("But only 1 man really want to success, it's Artem Zarubin!\n")

# ---------------------------------------------------------------------------------------------------------------------
enter_name_with_f = str(input("Enter your name: "))  # Using f strings for better experience
enter_surname_with_f = str(input("Enter your surname: "))
enter_age_with_f = int(input("Enter your age: "))
print(f"Name: \'{enter_name_with_f}\', surname: \'{enter_surname_with_f}\' and age: \'{enter_age_with_f}\'.")
print()

# ---------------------------------------------------------------------------------------------------------------------
day_today = dt.datetime.now()  # Using datetime module for first time to see what data is it today
time_now = day_today.time()  # Using datetime module for second time to see what time is now
print(f"Today's data: {day_today:%m-%d-%Y}")
print(f"Time now: {time_now:%T}")
print()

# ---------------------------------------------------------------------------------------------------------------------
try:  # Using catch block for first time
    enter_error = int(input("Enter any number to crash: "))
    enter_error += 15
    print(f"Your number + 15 = {enter_error}")
except ValueError:
    print("Enter number and not a string!")
print()

# ---------------------------------------------------------------------------------------------------------------------
false_until_try = True  # Updated input of numbers
enter_exception = None
while false_until_try:
    try:
        enter_exception = int(input("Enter any number, but not a string: "))
        false_until_try = False
        print(f"Your number is {enter_exception}")
    except ValueError:
        print(f"Please enter correct value!\n")
print()

# ---------------------------------------------------------------------------------------------------------------------
try:
    first_division = int(input("Input first number for divide it: "))
    second_division = int(input("Input second number for divide it: "))
    print(f"Result of your division is {first_division / second_division}")
except ValueError:
    print(f"You entered not a number!")
except ZeroDivisionError:
    print(f"You tried to divide by zero!")
print()

# ---------------------------------------------------------------------------------------------------------------------
try:  # Last example of try
    maximum_power_try = int(input("Enter any num for mega boss: "))
except ValueError:
    print(f"I said number and not a string!")
else:
    print(f"You hit boss for {maximum_power_try} xp!!!")
print()

# ---------------------------------------------------------------------------------------------------------------------
# Using sleep from time module
time.sleep(0.0001)
# bomb_timer = 3
# while bomb_timer > 0:
#     print(f"Explosion in {bomb_timer}...")
#     time.sleep(1)
#     bomb_timer -= 1
# print(f"*BOOOOOM*")
# print()

# ---------------------------------------------------------------------------------------------------------------------
print(f"Path to file: {sys.path}")  # Using sys and os modules
print(f"Secret name of your os: {os.name}")
print(f"You are using: {platform.system()}")
print()

# ---------------------------------------------------------------------------------------------------------------------
try:
    enter_math_sqrt = int(input("Enter any number to root it: "))
except ValueError:
    print("Wrong format!")
else:
    print(f"Root of your number \'{enter_math_sqrt}\' is {sqrt(enter_math_sqrt)}")
print()

# ---------------------------------------------------------------------------------------------------------------------
print(
    f"{my_module.hello_func()} Using my module for first time. My name is {my_module.name} and I've created {my_module.company_name}")
print()

# ---------------------------------------------------------------------------------------------------------------------
cowsay.cow("Devult is the best company, even animals now this!")
print(cowsay.get_output_string('trex', 'Yes, Devult is the best!'))
print()


# ---------------------------------------------------------------------------------------------------------------------
class Turtle:  # Creating class for first time
    name = None
    age = None
    color = None

    def __init__(self, name=None, age=None, color=None):
        self.set_data(name, age, color)

    def set_data(self, name=None, age=None, color=None):
        self.name = name
        self.age = age
        self.color = color

    def get_data(self):
        print(f"Name is {self.name}, Age is {self.age}, Color is {self.color}")


turtle_John = Turtle()
turtle_John.name = "John"
turtle_John.age = 76
turtle_John.color = "Brown"

turtle_Loo = Turtle()
turtle_Loo.name = "Loo"
turtle_Loo.age = 13
turtle_Loo.color = "Green"
print(f"Names of my turtles are {turtle_Loo.name} and {turtle_John.name}!")
print()

# ---------------------------------------------------------------------------------------------------------------------
turtle_create = Turtle()    # Using full access to class
name_of_turtle = str(input("Enter name of a turtle: "))
age_of_turtle = None
check_correct_name = True
while check_correct_name:
    try:
        age_of_turtle = int(input("Enter age of a turtle: "))
    except ValueError:
        print("Please enter number, and not a string data!\n")
    else:
        check_correct_name = False

color_of_turtle = str(input("Enter color of a turtle: "))
turtle_create.set_data(name_of_turtle, age_of_turtle, color_of_turtle)
print(
    f"We've created a new turtle! Name = {turtle_create.name}, Age = {turtle_create.age}, Color = {turtle_create.color}")
print()

# ---------------------------------------------------------------------------------------------------------------------
print(f"Showing info about turtle:")    # Using method to show data
turtle_Loo.get_data()
print()

# ---------------------------------------------------------------------------------------------------------------------
empty_turtle = Turtle() # Deafult data about class
print(f"Name of a turtle by default = {empty_turtle.name}, Age of the turtle by default = {empty_turtle.age} and Color = {empty_turtle.color}")
print()


# ---------------------------------------------------------------------------------------------------------------------
class Car:  # Quite a lot of subclasses about cars
    brand = None
    place_of_creation = None
    date_of_create = None

    def __init__(self, brand="Lamborghini", place_of_creation="Italy", date_of_create="4.12.2017"):
        self.brand = brand
        self.place_of_creation = place_of_creation
        self.date_of_create = date_of_create

    def get_info(self):
        print(f"{self.brand} was created in {self.place_of_creation} at {self.date_of_create}")


class Luxury(Car):
    cost = 100000
    doors = 4
    passenger_seats = 5
    weight = None


class SportUtilityVehicle(Car):
    cost = 0
    doors = 0
    passenger_seats = 0
    weight = None

    def __init__(self, brand, place_of_creation, date_of_create):
        super(SportUtilityVehicle, self).__init__(brand, place_of_creation, date_of_create)
        self.cost = 500000
        self.doors = 4
        self.passenger_seats = 8
        self.weight = None

    def get_info(self):
        super().get_info()
        print(f"And cost {self.cost}")


class Coupe(Car):
    pass


aston_martin_bowmore = Car("Aston Martin Bowmore", "England", "15.01.1913")
aston_martin_bowmore.get_info()

cadillac_eldorado = Luxury("Cadillac Eldorado 1969", "USA", "22.08.1902")
cadillac_eldorado.weight = 4000
cadillac_eldorado.get_info()

lamborghini_urus = SportUtilityVehicle("Lamborghini Urus", "Italy", "4.12.2017")
lamborghini_urus.weight = 6000
lamborghini_urus.doors = 6
lamborghini_urus.cost = 300000
lamborghini_urus.get_info()
print()


# ---------------------------------------------------------------------------------------------------------------------
def validator(func):    # Wrapping function
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Incorrect URL")

    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)


url_enter = input("Input any URL: ")
open_url(url_enter)
print()

# ---------------------------------------------------------------------------------------------------------------------
list_of_stars = []  # Just funny things with loops
for i in range(10):
    list_of_stars.append('*')

for rows in range(len(list_of_stars)):
    for col in range(len(list_of_stars)):
        print('*', end="   ")
    list_of_stars.pop()
    print()
print()

# ---------------------------------------------------------------------------------------------------------------------
print(f"Thanks all for seeing this perfect sh*t. THAT'S IT I GUESS =)")
