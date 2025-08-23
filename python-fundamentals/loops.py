# COUNTING POSITIVE NUMBERS
numbers = [1, -2, 3, 4, -5, 6, -7, 8]
count = 0

for i in numbers:
    if i > 0:
        count += 1

print("The number of positive numbers is:", count)

# Output:
# The number of positive numbers is: 5

# ------------------------------------------------------------------------------------------------------------------

# SUM OF EVEN NUMBERS
n = int(input("Enter the number till which you want to accumulate the sum of even numbers: "))

sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i
print("The sum of even numbers till", n, "is:", sum)

# Example Run:
# Enter the number till which you want to accumulate the sum of even numbers: 10
# The sum of even numbers till 10 is: 30

# ------------------------------------------------------------------------------------------------------------------

# MULTIPLICATION TABLE PRINTER
n = int(input("Enter the number for which you want to print the multiplication table: "))

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(n, " X ", i, " = ", n * i)

# Example Run:
# Enter the number for which you want to print the multiplication table: 3
# 3  X  1  =  3
# 3  X  2  =  6
# 3  X  3  =  9
# 3  X  4  =  12
# 3  X  6  =  18
# 3  X  7  =  21
# 3  X  8  =  24
# 3  X  9  =  27
# 3  X  10  =  30

# ------------------------------------------------------------------------------------------------------------------

# REVERSE A STRING USING LOOP
str_val = input("Enter the string : ")

reversed_str = ""

for i in str_val:
    reversed_str = i + reversed_str

print("Reversed string is :", reversed_str)

# Example Run:
# Enter the string : hello
# Reversed string is : olleh

# ------------------------------------------------------------------------------------------------------------------

# FIND THE FIRST NON REPEATED CHARACTER
str_val = input("Enter the string : ")

for i in str_val:
    if str_val.count(i) == 1:
        print("The first non repeated character is :", i)
        break
else:
    print("There is no non-repeating character")

# Example Run:
# Enter the string : swiss
# The first non repeated character is : w

# ------------------------------------------------------------------------------------------------------------------

# FACTORIAL CALCULATOR USING WHILE LOOP
n = int(input("Enter the number of which you want to know the factorial : "))

ans = 1
while n > 1:
    ans *= n
    n -= 1
print("The factorial of the given number is :", ans)

# Example Run:
# Enter the number of which you want to know the factorial : 5
# The factorial of the given number is : 120

# ------------------------------------------------------------------------------------------------------------------

# VALIDATE INPUT
# Keep asking until input is between 1 and 10
while True:
    n = int(input("Please enter a number (1-10): "))
    if n in range(1, 11):
        print("You entered a valid input:", n)
        break

# Example Run:
# Please enter a number (1-10): 15
# Please enter a number (1-10): 7
# You entered a valid input: 7

# ------------------------------------------------------------------------------------------------------------------

# PRIME NUMBER CHECKER
n = int(input("Enter the number : "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print(n, "is a Prime Number.")
else:
    print(n, "is not a Prime Number.")

# Example Run:
# Enter the number : 7
# 7 is a Prime Number.

# ------------------------------------------------------------------------------------------------------------------

# LIST UNIQUENESS CHECKER
items = ["apple", "banana", "guava", "apple", "banana"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate :", item)
        break
    unique_items.add(item)

# Output:
# Duplicate : apple

# ------------------------------------------------------------------------------------------------------------------

# EXPONENTIAL BACKOFF
# Problem --> Implement an exponential backoff strategy that doubles the wait time between retries,
#             starting from one second, but stops after 5 retries
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt :", attempts + 1, "- wait time :", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

# Output:
# Attempt : 1 - wait time : 1
# Attempt : 2 - wait time : 2
# Attempt : 3 - wait time : 4
# Attempt : 4 - wait time : 8
# Attempt : 5 - wait time : 16
