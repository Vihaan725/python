"""Write a program to check the application of not equal operator

"""
# 1) Store values in `a`, `b`, and `c`.

# 2) Check an AND condition using `a and b and c`:
#    - This becomes True only if all three values are treated as True.
#    - If the condition is True, print the “all true” message.
#    - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.

# 4) Check an OR condition: `a > 0 or b > 0`
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.

a = 10
b = 12 
c = 12

print(a != b)
print(b != c)
a = "python"
b = "coding"
if a != b : 
    print(a, 'and', b, 'are different')
a = 4
a = 5
if(a==1) != (b==5):
    print("Hello")
a=int(input("enter a number: "))
if a%2 != 0: 
    print(a, "is not an even number")
