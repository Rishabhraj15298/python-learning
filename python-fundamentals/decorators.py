# TIMING FUNCTION EXECUTION

# Problem --> Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {round(end - start,2)} time.")
        return result
    return wrapper

@timer 
def example_function(n):
    time.sleep(n) 

example_function(2)

# Output:
# Function 'example_function' took 2.0 time.

# ------------------------------------------------------------------------------------------------------------------

# Debugging Function Calls

# Problem --> Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwarg_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with args {arg_value} and kwargs {kwarg_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Rishabh", greeting="hi")

# Output:
# Calling greet with args Rishabh and kwargs greeting = hi
# hi, Rishabh!

# ------------------------------------------------------------------------------------------------------------------

# Cache return Values 

# Problem --> Implement a decorator that caches the return value of a function , so that when it's called
#             with the same arguments again, it returns the cached value instead of recomputing it.

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            print("Returning cached value")
            return cache_value[args]
        else:
            result = func(*args)
            cache_value[args] = result
            return result
    return wrapper

@cache
def compute_square(n):
    time.sleep(2)
    return n * n

print(compute_square(4))  # Takes time on first call
print(compute_square(4))  # Returns cached value immediately
print(compute_square(5))  # Takes time on first call  

# Output:
# 16            (after ~2 sec delay)
# Returning cached value
# 16
# 25            (after ~2 sec delay)
