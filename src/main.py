from datetime import date 
from utils import add , subtract , multiply , division
print("Name : Md. Tamim Khan")
print("Date: ",date.today())
print("Addition :",add(20,10))
print("Subtraction :",subtract(20,5))
print("Multiply :",multiply(20,10))
print("Division :",division(20,5))
print("Division by Zero:", division(10, 0))