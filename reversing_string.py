# 1) Ask the user to enter a number and store it in `n`.

# 2) Set `sum` to 0.

# (This will store the running total.)

# 3) Use a `for` loop from 1 to `n` (inclusive):

# - In each step, add the current value of `i` to `sum`.

# 4) After adding, print the current value of `sum`.

# (So the user can see how the sum increases step by step.)

n = int(input("Enter a value: "))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)
    
# 1) Ask the user to enter a word or sentence and store it in `string`.

# 2) Create an empty string called `string2`.

# (This will store the reversed version.)

# 3) Loop through each character `i` in `string`:

# - Add the character `i` in front of `string2`

# - This builds the reversed string step by step.

# 4) Print the original string (`string`).

# 5) Print the reversed string (`string2`).
string = str(input("Enter a word or sentence: "))
string2 = ""
for i in string:
    string2 = i + string2
print(string)
print(string2)