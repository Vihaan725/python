"""Write a program to check whether the given values have boolean values or not.

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
c = 0

if a and b and c:
    print("All the numbers have a boolean value of True")
else:
    print("At least one number has a boolean value of False")

a = 10
b = -10
c = 0

if a>0 or b>0 or c>o:
    print("Either of the numbers are greater than zero")
else:
    print("No number is greater than 0")

