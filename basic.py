
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print("Largest:", max(x, y, z))



def square(num):
    return num * num
print("Square of 5:", square(5))



n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
op = input("Enter operator (+ or -): ")
if op == "+":
    print("Result:", n1 + n2)
elif op == "-":
    print("Result:", n1 - n2)
else:
    print("Invalid operator")
