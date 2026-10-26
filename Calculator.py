#Calculator.py
user = input("Enter UserName: ")
menu = """
========================================
     AVAILABLE ARITHMETIC OPERATORS     
========================================
 [ +  ] : Addition
 [ -  ] : Subtraction
 [ *  ] : Multiplication
 [ /  ] : Division
 [ ** ] : Exponentiation (Power)
 [ // ] : Floor Division
 [ %  ] : Modulus (Remainder)
========================================
"""
#banner
print(20 * "*")
print()
print("Calculator")
print()
print(20 * "*")
print()
print(f"Hi: {user}")
#The Program
num_1 = float(input("Enter The First number: "))
print(menu)
arithmetic_opra = input("Enter Arithmetic operations: ")
num_2 = float(input("Enter The Second number: "))

if num_1 == 0 or num_2 == 0 and arithmetic_opra in ["/","//","%"]:
    print("Error: Cannot divide by zero!")
elif arithmetic_opra == "+":
    print(num_1 + num_2)
elif arithmetic_opra == "-":
    print(num_1 - num_2)
elif arithmetic_opra == "*":
    print(num_1 * num_2)
elif arithmetic_opra == "/":
    print(num_1 / num_2)
elif arithmetic_opra == "**":
    print(num_1 ** num_2)
elif arithmetic_opra == "//":
    print(num_1 // num_2)
elif arithmetic_opra == "%":
    print(num_1 % num_2)
else:
    print("Arithmetic operations value error")