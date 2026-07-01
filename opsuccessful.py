'''Write a program that:
Accepts a number from the user.
Converts it to an integer.
Divides 100 by that number.
Handle both:
ValueError
ZeroDivisionError
Print "Operation Successful" if no exception occurs.
Use a finally block to print:'''
try:
    x = int(input("Enter a number: "))
    x = x/100
except ValueError:
    print("The number is invalid")
except ZeroDivisionError:  
    print("The number is divided by zero. ")
finally:
    print("Operation Successfull")