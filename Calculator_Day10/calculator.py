import art
# Add
def add(n1,n2):
	return n1 + n2

# subtract
def subtract(n1,n2):
	return n1 - n2

# Multiply
def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
    }

while True:	
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    while True:
        for operation in operations:
            print(operation)
        op = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
    

        def calculation(opValue):
            return operations[opValue](num1, num2)
            # if op == '+':
            #     return add(num1, num2)
            # elif op == '-':
            #     return subtract(num1, num2)
            # elif op == '*':
            #     return multiply(num1, num2)
            # elif op == '/':
            #     return divide(num1, num2)


        result = calculation(op)
        print(f"{num1} {op} {num2} = {result}")
        response = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
        if response == 'y':
            num1 = result
            continue
        else:
            break
print(result)
