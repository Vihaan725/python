try:
    num = int(input("Enter a number: "))
    if num%2==0:
        print("The number is even")
except ValueError:
    print("the number is invalid")