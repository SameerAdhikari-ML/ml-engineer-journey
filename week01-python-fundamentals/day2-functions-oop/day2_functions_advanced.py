# ============================================
# DAY 2: Advanced Functions
# Name: Sameer Adhikari
# Date: December 31, 2025
# ============================================

# PART 1: *args and **kwargs (15 min)
# --------------------------------------------

# Exercise 1: Variable number of arguments
def sum_all(*args):
    """Sum any number of arguments"""
    # TODO: Use *args to sum all numbers passed
    return sum(args)

# Test:
print(sum_all(1, 2, 3))  # Should return 6
print(sum_all(10, 20, 30, 40))  # Should return 100


# Exercise 2: Keyword arguments
def print_info(**kwargs):
    """Print all keyword arguments"""
    # TODO: Loop through kwargs and print key: value pairs
    a= [f"{key} : {values}" for key,values in kwargs.items()]
    return a
        

# Test:
print(print_info(name="Sameer", age=21, city="Kathmandu"))


# Exercise 3: Mix both
def student_info(name, *scores, **details):
    """
    name: required argument
    scores: variable test scores
    details: additional info like city, college, etc.
    """
    # TODO: Print name, calculate average of scores, print details
    score = sum(scores) / len(scores)
    print(f"name: {name}")
    print(f"scores: {score}")
    for key,values in details.items():
        print(f"{key}: {values}")

# Test:
student_info("Sameer", 85, 90, 78, 92, city="Kathmandu", college="ABC")


# PART 2: Lambda Functions (10 min)
# --------------------------------------------

# Exercise 4: Simple lambda
# TODO: Create a lambda that squares a number
square = lambda x: x **2  # Replace with lambda

# Test:
print(square(5))  # Should print 25


# Exercise 5: Lambda with map
numbers = [1, 2, 3, 4, 5]
# TODO: Use lambda with map() to double all numbers
doubled = map(lambda x: x*2, numbers)  # Use map and lambda

# Test:
print(list(doubled))  # [2, 4, 6, 8, 10]


# Exercise 6: Lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# TODO: Use lambda with filter() to get only even numbers
evens = filter(lambda x: x%2 ==0, numbers)  # Use filter and lambda

# Test:
print(list(evens))  # [2, 4, 6, 8, 10]


# Exercise 7: Sort with lambda
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
# TODO: Sort students by grade (highest first) using sorted() and lambda
sorted_students = sorted(students, key = lambda x : x["grade"], reverse= True)

# Test:
print(sorted_students)


# PART 3: Decorators (Basic) (15 min)
# --------------------------------------------

# Exercise 8: Simple decorator
def my_decorator(func):
    """A simple decorator that prints before and after function call"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# TODO: Apply this decorator to a function using @my_decorator
# Create a function say_hello() that prints "Hello!"
def say_hello():
    print("Hello!")
my_decorator(say_hello)()

# Exercise 9: Decorator with arguments
def repeat(times):
    """Decorator that repeats function call"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # TODO: Call func 'times' number of times
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

# TODO: Create a function greet(name) and use @repeat(3) on it
def greet(name):
    print(f"Hello! {name}")
 
repeat(3)(greet)("SawN")


# PART 4: Practice Problems (20 min)
# --------------------------------------------

# Challenge 1: Create a function that accepts any number of numbers
# and returns a dictionary with sum, average, min, max
def analyze_numbers(*numbers):
    """Return dict with sum, avg, min, max of all numbers"""
    a = {}
    a["sum"] = sum(numbers)
    a["avg"] = sum(numbers) / len(numbers)
    a["min"] = min(numbers)
    a["max"] = max(numbers)
    
    return a


# Test:
print(analyze_numbers(10, 20, 30, 40, 50))
# Should return: {'sum': 150, 'avg': 30.0, 'min': 10, 'max': 50}


# Challenge 2: Create a function calculator that takes operation as string
# and variable number of numbers, performs the operation
def calculator(operation, *numbers):
    """
    operation: 'sum', 'multiply', 'max', 'min'
    numbers: any number of values
    """
    if operation == "sum":
        return sum(numbers)
    elif operation == "multiply":
        a = 1 
        for i in numbers:
            a *= i
        return a
    elif operation == "min":
        return min(numbers)
    elif operation == "max":
        return max(numbers)
    else:
        return "Please choose correct operations!!!"
    
# Test:
print(calculator('sum', 1, 2, 3, 4))  # 10
print(calculator('multiply', 2, 3, 4))  # 24


# Challenge 3: Higher-order function
def apply_operation(numbers, operation):
    """
    Apply an operation (function) to each number in list
    numbers: list of numbers
    operation: a function to apply
    """
    return list(map(operation,numbers))

# Test:
print(apply_operation([1, 2, 3, 4], lambda x: x ** 2))
# Should return: [1, 4, 9, 16]

# ============================================
# COMPLETION STATS
# ============================================
# Exercises completed: 12/12 ✅
# Time taken: 20-30 min
# Hardest exercise: "None, all were clear"
# What I learned: 
# - How to use *args and **kwargs for flexible function arguments.
# - Creating and using lambda functions for concise operations.
# - Writing decorators to modify function behavior.
# ============================================