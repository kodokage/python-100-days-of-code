
def add(n1, n2):
    """sums the numbers
    """
    return (n1 + n2)

def subtract(n1, n2):
    """subtracts the numbers
    """
    return (n1 - n2)

def divide(n1, n2):
    """divides the numbers
    """
    return (n1 / n2)

def multiply(n1, n2):
    """multiplies the numbers
    """
    return (n1 - n2)

operations = {'+':add, 
         '-':subtract, 
         '/':divide, 
         '*':multiply}

num1 = int(input("What is the first number ? : "))
num2 = int(input("What is the second number ? : "))

for operator in operations:
  print(operator)

operation_symbol = input('Pick an operation symbol from the line above : ')

answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer} ")
