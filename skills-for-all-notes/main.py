# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')


# print(2**2)
# print(2**2**2)
# print(4//3)
# print(4%3)
# print(0.01*(2**30))
# print('Brian\'s a man so he\'s already grown
# up') # Blackslash(\) serve para poder utilizar ' ou " dentro de outras ' ou " em uma string
# print('new \nline')
# print("""   just testing new lines insane""")
# print("oi" + 'sou lindo')
# print("2" + "2")
# print("multplierenre" * 9)
# print("4\n" * 4)

# def working_w_variables(x):
#    print(x)
#    print(x + 3)
#
#    y = 'test'
#    print(y + '!')

#    y = 34
#    print(y)


# working_w_variables(7)

# x = input("Insert your name: ")
# print(x)

# x = int(input("Insert a number: "))
# print(x)

# age = 42
# print("His age is " + str(age))

# x = "spam"
# x += "test"
# print(x)

# Walrus operator := allows you to assign values to variables within an expression, including variables that do not
# exist yet.
# print(num := int(input("Insert a number")))
#
#
# print("My name is ", end="")
# print("Monty Python.")
#
# print("My", "name", "is", "Monty", "Python.", sep="-")
#
# print(0o123)
#
# print(0xb15)
#
# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5
# print("c =", c)
#
#
# kilometers = 12.25
# miles = 7.38
#
# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers / 1.61
#
# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#
#
# x = 0
# x = float(x)
# y = 3 * x**3 - 2 * x**2 + 3 * x - 1
# print("y =", y)
#
# x = 1
# x = float(x)
# y = 3 * x**3 - 2 * x**2 + 3 * x - 1
# print("y =", y)
#
# x = -1
# x = float(x)
# y = 3 * x**3 - 2 * x**2 + 3 * x - 1
# print("y =", y)

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# mins = mins + dura # find a total of all minutes
# hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
# mins = mins % 60 # correct minutes to fall in the (0..59) range
# hour = hour % 24 # correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')
#
# if 10 > 5:
#     print("true")
#
#
# if 10 < 9:
#     print("true")
# else:
#     print("false")
#
# if the_weather_is_good:
#     if nice_restaurant_is_found:
#        have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()
#
# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()

# number1 = int(input("Enter the first number"))
# number2 = int(input("Enter the second number"))
#
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# print("The larger number is:", larger_number)
#
#
# # Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.
#
# largest_number = max(number1, number2, number3) #min() returns the lowest number
#
# # Print the result.
# print("The largest number is:", largest_number)

# strInput = input("Insert a string:")
# if strInput == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever")
# elif strInput == "spathiphyllum":
#     print("No, i waint a big Spathiphyllum")
# else:
#     print("Spathiphyllum! Not " + strInput + "!")


# Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people
# paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for
# short) had to be paid once a year, and was evaluated using the following rule:
#
# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556
# thalers and 2 cents (this was what they called tax relief) if the income was higher than this amount, the tax was
# equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers. Your task is to write a tax
# calculator.
#
# It should accept one floating-point value: the income. Next, it should print the calculated tax, rounded to full
# thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code
# in the editor. Note: this happy country never returned any money to its citizens. If the calculated tax was less
# than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your
# calculations.
#
# income = float(input("What is the citizen's income?"))
#
# if income < 85528:
#     tax = income * 0.18 - 556.02
# else:
#     tax = 14839.02 + 85528 * 0.32
#
# if tax < 0.0:
#     tax = 0.0
#
# tax = round(tax, 0)
# print(tax)

# year = int(input("Insert the year"))
# if year < 1582:
#     print("not within grego calendar")
# else:
#     if year % 4 != 0:
#         print("It's a common year")
#     elif year % 100 != 0:
#         print("leap year")
#     elif year % 400 != 0:
#         print("common")
#     else:
#         print("leap")

# A program that reads a sequence of numbers and counts how many numbers are even or odds
# odd_numbers = 0
# even_numbers = 0
#
# number = int(input("Enter a number or type 0 to stop: "))
#
# while number != 0:
#     #check if number is odd
#     if number % 2 == 1:
#         #Increase the odd_numbers counter
#         odd_numbers += 1
#     else:
#         #Increase de even numbers counter
#         even_numbers += 1
#
#     number = int(input("Enter a number or type 0 to stop: "))
#
# print("Odd numbers: ", odd_numbers)
# print("Even numbers:", even_numbers)

# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """
# )
# number = int(input("Enter the number: "))
#
# while number != secret_number:
#     print("Ha ha! You're stuck in my loop!")50
#     number = int(input("Enter the number again: "))
# print(secret_number, "Well done, muggle! You are free now.")

# for i in range(2, 8):
#     print(i)

# for i in range(0, 30, 3):
#     print(i)

# power = 1
# for i in range(16):
#     print("2 to the power of", i, "is", power)
#     power *= 2

# import time
# for second in range(1, 6):
#     print(second, "Mississippi")
#     time.sleep(1)
#
# print("Ready or not, here i come!")


# #Break Example
# largest_number = -99999999
# counter = 0
#
# while True:
#     number = int(input("Enter a number or type -1 to end the program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# Continue Example
# number = int(input("Enter a number or type -1 to end program: "))
#
# while number != -1:
#     if number == -1:
#         continue
#     counter += 1
#
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end the program: "))
#
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# while True:
#     word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
#     if word == "chupacabra":
#         break
# print("You've successfully left the loop!")


# THE UGLY VOWEL EATER
# user_word = input("Enter a word: ")
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         print(letter)


# THE PRETTY VOWEL EATER
# word_without_vowels = ""
#
# user_word = input("Enter your word: ")
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         word_without_vowels += letter
#
# print(word_without_vowels)

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)
#
# i = 5
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

# for i in range(5):
#     print(i)
# else:
#     print("else:", i)

# i = 111
# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)

# blocks = int(input("Enter the number of blocks: "))
#
# height = 0
# in_layer = 1
# while in_layer <= blocks:
#     height += 1
#     blocks -= in_layer
#     in_layer += 1
#
# print("The height of the pyramid:", height)

# c0 = int(input("Enter c0: "))
#
# if c0 > 1:
#     steps = 0
#     while c0 != 1:
#         if c0 % 2 != 0:
#             cnew = 3 * c0 + 1
#         else:
#             cnew = c0 // 2
#         print(c0)
#         c0 = cnew
#         steps += 1
#     print("steps =", steps)
# else:
#     print("Bad c0 value")

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")


# shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, shifting one bit to
# the right is like dividing by two

# 17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as
# integer division by two)

# 17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as
# integer multiplication by four)

# var = 17
# var_right = var >> 1 #divides var by 1 >> (2)
# var_left = var << 2 #multiplies var by 2 * 2 = >>
# print(var, var_left, var_right)

# LISTS

# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
#
# numbers[0] = 111
# print("\nPrevious list content:", numbers)  # Printing previous list content.
#
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("Previous list content:", numbers)  # Printing previous list content.
#
# print("\nList's length:", len(numbers))  # Printing previous list length.
#
# del numbers[1]  # Removing the second element from the list.
# print("New list's length:", len(numbers))  # Printing new list length.
# print("\nNew list content:", numbers)  # Printing current list content.
#
# print(numbers[-1]) # Printing the last element on the list
# print(numbers[-2]) # Printing the one before last in the list

# Scenario
#
# numbers = [1, 2, 3, 4, 5]
#
# numbers[2] = int(input("Enter an integer number"))
#
# del numbers[-1]
#
# print(len(numbers))

# Add elements to a list append() or insert()
# append add the value to the end of the list: list.append(value)
# insert() add the value at any place of the list: list.insert(location, value)
#
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
#
# numbers.append(4)
#
# print(len(numbers))
# print(numbers)
#
# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# append
# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.append(i + 1)
#
# print(my_list)

# insert
# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.insert(0, i + 1)
#
# print(my_list)

# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in range(len(my_list)):
#     total += my_list[i]
#
# print(total)
#
# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in my_list:
#     total += i
#
# print(total)
#
# my_list = [10, 1, 8, 3, 5]
#
# length = len(my_list)
#
# print(length // 2)
#
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
#
# print(my_list)

# beatles = []
# print("Step 1:", beatles)
#
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)
#
# for i in range(2):
#     beatles.append(input("New band member: "))
#
# print("Step 3:", beatles)
#
# # step 4:
# del beatles[-1]
# del beatles[-1]
# print("Step 4:", beatles)
#
# # step 5:
# beatles.insert(0, "RingoStarr")
# print("Step 5:", beatles)
# print("The Fab:",len(beatles))
#
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
#
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)

# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print("\nSorted:")
# print(my_list)

# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)

# my_list = [8, 10, 6, 2, 4]
# my_list.reverse()
# print(my_list)

# COPY LIST
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)
#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:]
# print(new_list)
#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)
#
# my_list = [0, 3, 12, 8, 2]
#
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
#
# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
#
# print(largest)

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
#
# for i in my_list:
#     if i > largest:
#         largest = i
#
# print(largest)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
#
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
#
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")

# my_list = [1, 2, 3, 2, 3, 1, 5, 4, 4, 6, 7, 9, 6]
# new_list = []
#
# for number in my_list:
#     if number not in new_list:
#         new_list.append(number)
# my_list = new_list[:]
# print(my_list)

# simple for
# row = [7 for i in range(8)]
# print(row)

# squares = [x ** 2 for x in range(10)]
# print(squares)

# twos = [2 ** i for i in range(8)]

# odds = [x for x in squares if x % 2 != 0 ]
#
# print(odds)

# vacancy = 0
#
# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#
# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1
# print(vacancy)


# Cube - a three-dimensional array (3x3x3)
#
# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],
#
#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],
#
#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]
#
# print(cube)
# print(cube[0][0][0])  # outputs: ':('
# print(cube[2][2][0])  # outputs: ':)'


# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)


# t = [[3 - i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
#
#     print(s)
# print(t)
# print(s)

############################

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)


s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)


##############################

# Ex. 1
def subtra(a, b):
    print(a - b)


subtra(5, 2)  # outputs: 3
subtra(2, 5)  # outputs: -3


# Ex. 2
def subtra(a, b):
    print(a - b)


subtra(a=5, b=2)  # outputs: 3
subtra(b=2, a=5)  # outputs: 3


# Ex. 3
def subtra(a, b):
    print(a - b)


subtra(5, b=2)  # outputs: 3
subtra(5, 2)  # outputs: 3


########################
# Check if year is leap


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


############################

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

############################

print("just testing this one")

############################


def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))

# backslash (\) symbol is used. If you use it in Python code and end a line with it,
#  it will tell Python to continue the line of code in the next line of code.

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

####################################

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

####################################################################

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

