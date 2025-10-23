
import math
print("Square Root of 25:", math.sqrt(25))
print("2^3:", math.pow(2, 3))
print("PI Value:", math.pi)
print("Factorial of 5:", math.factorial(5))
print("Sin 90°:", math.sin(math.radians(90)), "\n")


import random
print("Random number (1-10):", random.randint(1, 10))

fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Random choice:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled list:", fruits, "\n")


from datetime import datetime, timedelta

now = datetime.now()
print("Current Time:", now)
print("Formatted Date & Time:", now.strftime("%d-%m-%Y %I:%M %p"))

future = now + timedelta(days=7)
print("Date After 7 Days:", future, "\n")


import os

print("Current Directory:", os.getcwd())
print("Files in Directory:", os.listdir())

folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print("Folder Created:", folder_name)
else:
    print("Folder already exists:", folder_name)

print()


import sys
print(">> SYS PACKAGE")

print("Python Version:", sys.version)
print("Python Executable Path:", sys.executable)
print("Command-line Arguments:", sys.argv)

