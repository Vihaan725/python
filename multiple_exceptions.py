try:
    num1, num2 = eval(input("Etner two numbers, seperated by a coma: "))
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error!")
except SyntaxError:
    print("Comma is missing, Enter the numbers seperated by coma.")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will excecute no matter what. ")