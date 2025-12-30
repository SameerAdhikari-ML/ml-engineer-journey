# ============================================
# DAY 1: Python Basics - Learn by Doing
# Name: Sameer Adhikari
# Date: December 30, 2025
# ============================================

# BLOCK 1: VARIABLES & TYPES (20 min)
# --------------------------------------------

# Exercise 1: Create 5 different types of variables
# TODO: Create a string variable with your name
# TODO: Create an integer variable with your age
# TODO: Create a float variable with your height
# TODO: Create a boolean variable (are you a student?)
# TODO: Create a list with 5 favorite foods

name = "Sameer Adhikari"
age = 21
height  = 5.8
student = True
fav_foods = ['momo', 'burger', 'pizza', 'kfc', 'keema noodles']

# TODO: Print all of them using f-strings

print(f"My name is {name} and I am {age} years old. My height is {height}.")
print(f"I am a student. {student}  My favorite foods are {fav_foods}.")

# Exercise 2: Type conversions
# TODO: Convert string "123" to integer
# TODO: Convert integer 50 to string
# TODO: Convert float 3.14 to integer (what happens?)
# TODO: Print the results

a = "123"
b = int(a)
c = 50 
d = str(c)
e = 3.14
f = int(3.14)
print(type(b),
      type(d),
      type(f))

# Exercise 3: String operations
# TODO: Create a sentence with your name
# TODO: Convert it to uppercase
# TODO: Convert it to lowercase
# TODO: Replace one word with another word
# TODO: Split the sentence into a list of words
# TODO: Print each result

sentence = "I am Sameer Adhikari."
uppercase = sentence.upper()
lowercase = sentence.lower()
replace = sentence.replace(" Adhikari.", ".")
split = sentence.split()
print(sentence)
print(uppercase)
print(lowercase)
print(replace)
print(split)


# BLOCK 2: MATH & OPERATORS (20 min)
# --------------------------------------------

# Exercise 4: Basic calculator
# TODO: Calculate 25 + 67
# TODO: Calculate 12 * 8
# TODO: Divide 100 by 7 (regular division)
# TODO: Divide 100 by 7 (integer division //)
# TODO: Find remainder when 17 is divided by 5 (%)
# TODO: Calculate 2 to the power of 10 (**)

additon = 25 +67
print(f"The addition of 25 and 67 is {additon}.")

multiplication = 12 * 8
print(f"The multiplication of 12 and 8 is {multiplication}.")

division = 100 / 7
print(f"The division of 100 and 7 is {division}.")

integer_division = 100 // 7  
print(f"The integer division of 100 and 7 is {integer_division}.")

remainder = 17 % 5
print(f"The remainder of 17 by 5 is {remainder}.")

power_of = 2 ** 10
print(f"2 to the power of 10 is {power_of}")

# Exercise 5: Area calculator
# TODO: Calculate area of rectangle (length=10, width=5)
# TODO: Calculate area of circle (radius=7, use pi=3.14159)
# TODO: Calculate area of triangle (base=6, height=8)

length = 10 
width = 5
area = length * width
print(f"The area of rectangle is {area}.")

radius = 7
pi = 3.14159
area = pi * (radius **2)
print(f"The area of circle is {area}.")

base = 6 
height = 8
area = 1/2 *(base * height)
print(f"The area of triangle is {area}.")

# Exercise 6: Temperature converter
# TODO: Convert 25 Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32

celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"The {celsius} degree celsius is {fahrenheit} degree fahrenheit.")


# TODO: Convert 77 Fahrenheit to Celsius
# Formula: C = (F - 32) * 5/9

fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(f"The {fahrenheit} degree fahrenheit is {celsius} degree celsius.")


# BLOCK 3: CONDITIONALS (30 min)
# --------------------------------------------

# Exercise 7: Even or odd checker
number = 42
# TODO: Write if/else to print "Even" or "Odd"

if ((number % 2) == 0 ):
    print(f'{number} is even number.')
else:
    print(f'{number} is odd number.')

# Exercise 8: Grade calculator
score = 85
# TODO: Write if/elif/else to determine grade
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60

if (score <= 100 and score >= 90 ):
    print("Congratulations you got 'A' grade.")
elif (score <= 89 and score >= 80 ):
    print("Congratulations you got 'B' grade.")
elif (score <= 79 and score >= 70 ):
    print("You got 'C' grade.")
elif (score <= 69 and score >= 60 ):
    print("You got 'D' grade.")
elif (score <= 60 ):
    print("You got 'F' grade.")
else:
    print("Invalid score.")

# Exercise 9: Age category
age = 25
# TODO: Print "Child" if age < 13
# "Teenager" if 13-19
# "Adult" if 20-59
# "Senior" if 60+

if age >= 60:
    print("Senior")
elif (age <= 59 and age >= 20):
    print("Adult")
elif (age <= 19 and age >= 13):
    print("Teenager")
elif (age < 13):
    print("Child")
else:
    print("Put your age in Number")

# Exercise 10: Number comparison
a = 15
b = 20
# TODO: Print which number is larger, or if equal

if a == b:
    print('Equal')
elif (a>b):
    print(f'{a} is larger.')
elif (a<b):
    print(f'{b} is larger.')

# Exercise 11: Leap year checker
year = 2023
# TODO: Check if it's a leap year
# Leap year if: divisible by 4 AND (not divisible by 100 OR divisible by 400)

if ((year %4) == 0 and ((year % 100) != 0 or (year % 400) == 0)):
    print(f"{year} is a Leap year.")
else:
    print(f"{year} is not a Leap year.")

# BLOCK 4: LOOPS (40 min)
# --------------------------------------------

# Exercise 12: Print numbers 1 to 10
# TODO: Use a for loop with range()

for i in range(10):
    print(i+1)

# Exercise 13: Print even numbers from 2 to 20
# TODO: Use for loop

for i in range(2,21,1):
    if (i %2 == 0):
        print(i) 

# Exercise 14: Countdown
# TODO: Print 10, 9, 8, ... 1, then "Blastoff!"

for i in range(10,-1,-1):
    if i == 0:
        print("Blastoff!")
        break
    print(i)

# Exercise 15: Sum of 1 to 100
# TODO: Use a loop to calculate the sum
# Don't use sum() function - do it manually with a loop

sum = 0
for i in range(1,101):
    sum += i
print(sum)

# Exercise 16: Multiplication table for 7
# TODO: Print 7x1=7, 7x2=14, ... 7x10=70
multiplication_table = 7
for i in range(1,11):
    print(f"{multiplication_table} x {i} = {multiplication_table * i}")

# Exercise 17: Pattern printing
# TODO: Print this pattern:
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print("*"*i)

# Exercise 18: Multiples of 3
# TODO: Print all multiples of 3 between 1 and 50

for i in range(1,51):
    if i %3 == 0:
        print(i)

# BLOCK 5: LISTS (40 min)
# --------------------------------------------

# Exercise 19: List basics
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# TODO: Print the first fruit
# TODO: Print the last fruit
# TODO: Print the length of list
# TODO: Add "fig" to the list
# TODO: Remove "banana" from the list
# TODO: Print the updated list

print(f"First fruit in list is {fruits[0]}.")
print(f"First fruit in list is {fruits[-1]}.")
print(f"Length of list is {len(fruits)}.")
fruits.append("fig")
print(fruits)
fruits.remove("banana")
print(fruits)

# Exercise 20: List operations
numbers = [10, 20, 30, 40, 50]
# TODO: Calculate sum of all numbers (don't use sum())
# TODO: Find maximum number (don't use max())
# TODO: Find minimum number (don't use min())
# TODO: Calculate average
a = 0
for i in numbers:
    a += i
print(a)

max_num = numbers[0]
min_num = numbers[0]

for i in numbers:
    if i >= max_num:
        max_num = i
    if i <= min_num:
        min_num = i

print(f"Maximum number in list is {max_num}")
print(f"Minimum number in list is {min_num}")

# Exercise 21: List searching
colors = ["red", "green", "blue", "yellow", "green"]
# TODO: Check if "blue" is in the list
# TODO: Count how many times "green" appears
# TODO: Find the index of "yellow"

if "blue" in colors:
    print("Blue is in the list")
else:
    print("Blue is not in the list")

green = 0
for i in colors:
    if "green" == i:
        green += 1
print(f"green appears {green} times.")
print(colors.index("yellow"))

# Exercise 22: List slicing
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# TODO: Print first 3 letters
# TODO: Print last 3 letters
# TODO: Print every other letter
# TODO: Print the list reversed

print(letters[:3])
print(letters[-3:])
for i in letters:
    print(i)
rev_list = []
for i in letters[::-1]:
    rev_list.append(i)
print(rev_list)

# Exercise 23: List of squares
# TODO: Create a list of squares from 1 to 10
# Example: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Try with a loop first

list_square = [i**2 for i in range(1,11)]
print(list_square)

# BLOCK 6: FUNCTIONS (50 min)
# --------------------------------------------

# Exercise 24: Simple greeting function
def greet(name):
    """Print a greeting message with the name"""
    print(f'Hello, Goood Morning {name}!!')

# TODO: Test it by calling greet("Alice") and greet("Bob")
greet("Sameer")

# Exercise 25: Addition function
def add_numbers(a, b):
    """Return the sum of a and b"""

    return a + b


# TODO: Test with print(add_numbers(5, 7))
print(add_numbers(5, 7))

# Exercise 26: Even checker function
def is_even(num):
    """Return True if num is even, False otherwise"""
    if num % 2 == 0 :
        return True
    else:
        return False

# TODO: Test with multiple numbers
print(is_even(5))
print(is_even(6))

# Exercise 27: Sum list function
def sum_list(numbers):
    """Return the sum of all numbers in the list"""
    a = 0
    for i in numbers:
        a += i
    return a


# TODO: Test with [1, 2, 3, 4, 5]
print(sum_list([1, 2, 3, 4, 5]))

# Exercise 28: Factorial function
def factorial(n):
    """
    Calculate factorial of n
    Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    a = 1
    for i in range(1,n+1):
        a *= i
    return a


# TODO: Test with factorial(5) and factorial(7)
print(factorial(5))
print(factorial(7))

# BLOCK 7: CHALLENGE PROBLEMS (60 min)
# --------------------------------------------

# Challenge 1: FizzBuzz
def fizzbuzz(n):
    """
    For numbers 1 to n, print:
    - "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - "FizzBuzz" if divisible by both
    - Otherwise the number itself
    """
    for i in range(1,n+1):
        if ((i %3 ==0) and (i %5== 0)):
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 ==0:
            print("Buzz")
        else:
            print(i)

# TODO: Test with fizzbuzz(20)
print(fizzbuzz(15))
print(fizzbuzz(20))

# Challenge 2: Fibonacci sequence
def fibonacci(n):
    """
    Return a list of first n Fibonacci numbers
    Example: fibonacci(7) should return [0, 1, 1, 2, 3, 5, 8]
    """
    a = []
    for i in range(n):
        if len(a)== 0 or len(a) == 1:
            a.append(i)
        
        else:
            a.append(a[-2] + a[-1])
    return a


# TODO: Test with fibonacci(10)
print(fibonacci(10))

# Challenge 3: Sum even numbers only
def sum_even_numbers(numbers):
    """Return sum of only even numbers in the list"""
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    return sum

# TODO: Test with [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (should return 30)
print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Challenge 4: Palindrome checker
def is_palindrome(text):
    """
    Check if text reads the same forwards and backwards
    Ignore spaces and case
    Example: "racecar" is palindrome, "hello" is not
    """
    a = "".join(text.lower().split())
    b = ""
    for i in a[::-1]:
        b += i
    if a == b:
        return f"'{text}' is palindrome"
    else:
        return f"'{text}' is not palindrome"


# TODO: Test with "racecar", "hello", "A man a plan a canal Panama"
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))

# Challenge 5: Prime number checker
def is_prime(n):
    """
    Check if n is a prime number
    Prime = only divisible by 1 and itself
    """
    if n ==2:
        return True
    if n<2:
        return False
    if (n% 2 == 0) or (n%3 ==0):
        return False
    for i in range(3,int(n**0.5)+1,2):
        if (n % i ==0):
            return False
    return True

# TODO: Test with 17 (True), 20 (False), 29 (True)
print(is_prime(25))
print(is_prime(17))
print(is_prime(20))
print(is_prime(29))
print(is_prime(1))

# Challenge 6: Find largest without max()
def find_largest(numbers):
    """Find and return the largest number without using max()"""
    max = numbers[0]
    for i in numbers:
        if i >= max:
            max = i
    return max


# TODO: Test with [3, 7, 2, 9, 1, 5] (should return 9)
print(find_largest([3, 7, 2, 9, 1, 5]))

# BONUS Challenge: Simple calculator
def calculator(num1, num2, operation):
    """
    Perform operation on num1 and num2
    operation can be: '+', '-', '*', '/'
    Return the result
    """
    if operation == "+":
        return num1 + num2
    elif operation == "/":
        return num1 / num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


# TODO: Test all 4 operations
print(calculator(10,5,'+'))
print(calculator(10,5,'-'))
print(calculator(10,5,'/'))
print(calculator(10,5,'*'))


# ============================================
# YOUR COMPLETION STATS
# ============================================
# How many exercises completed? ___/35
# Time taken: ___ hours
# Hardest exercise: ___
# What did you learn?
# ============================================