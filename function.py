
def greet():
    print("Hello! Welcome.")

greet()


def add(a, b):
    print("Addition:", a + b)

add(10, 5)


def multiply(a, b):
    return a * b

result = multiply(4, 3)
print("Multiplication:", result)


def welcome(name="Guest"):
    print("Welcome,", name)

welcome()  
welcome("Mehedi")  


def is_even(num):
    if num % 2 == 0:
        return True
    return False

print("Is 10 Even?", is_even(10))


def table(n):
    print(f"\nMultiplication Table of {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

table(5)


def print_list(items):
    print("\nYour List:")
    for item in items:
        print("-", item)

print_list(["Apple", "Banana", "Mango"])


def max_in_list(numbers):
    return max(numbers)

nums = [12, 35, 7, 56, 23]
print("\nMax number:", max_in_list(nums))


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
