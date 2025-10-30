# input_with_error_handling.py

try:
    n = int(input("enter a number:"))
except Exception:
    n = 1


for i in range(n):
    print("Welcome")


    