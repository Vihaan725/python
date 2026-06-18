def total_cal(bill_amount, tip_per):
    total = (bill_amount)*(1+0.01*tip_per)
    total = round(total, 2)
    print(total)
total_cal(150,20)
def cube(number):
    return (number**3)
def by_3(number):
    if number%3==0:
        return (cube(number))
    else:
        return (False)
print(by_3(9))
def factorial(x):
    '''This is a recursive function.'''
    if x==0 or x==1:
        return (1)
    else:
        return (x*factorial(x-1))
print(factorial.__doc__)
print(factorial(3))