# Step 1: Create a function named cube.
# Step 2: The function should accept one parameter:
# - number
# Step 3: Inside the function, calculate the cube of the number.
# Multiply the number by itself three times.
# Step 4: Return the calculated cube value.
# Step 5: End the function definition.
# --------------------------------------------------
# Step 6: Create another function named by_three.
# Step 7: The function should accept one parameter:
# - number
# Step 8: Check whether the number is divisible by 3.
# Step 9: If the number is divisible by 3:
# Call the cube function using the same number.
# Return the value received from the cube function.
# Step 10: Otherwise:
# Return False.
# Step 11: End the function definition.
# --------------------------------------------------
# Step 12: Display the result of calling by_three with 9
# Step 13: Display the result of calling by_three with 4.
# Step 14: Run the program and observe the output.
# Step 15: Verify that:
# - The cube is returned when the number is divisible by 3.
# - False is returned when the number is not divisible by 3.
def cube(number):
    x = number*number*number
    return x
def by_three(number):
    if number%3==0:
        y = cube(number)
        return y
    else:
        return False
by_three(9)
by_three(4) 
