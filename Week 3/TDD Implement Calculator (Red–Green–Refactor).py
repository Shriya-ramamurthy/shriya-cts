class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

calc = Calculator()

print("Addition:", calc.add(20, 10))
print("Subtraction:", calc.subtract(20, 10))
print("Multiplication:", calc.multiply(20, 10))
print("Division:", calc.divide(20, 10))

#python Calculator.py

#Addition: 30
#Subtraction: 10
#Multiplication: 200
#Division: 2.0