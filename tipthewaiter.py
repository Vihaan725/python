"""Let's create a function total_calc() that helps us calculate and print out the total amount paid
at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us
tip (tip_perc ), this function calculates the total amount you should pay."""
"""# Step 1: Create a function to calculate the final bill amount.
# Step 2: The function should accept two parameters:
# - bill_amount
# - tip_percentage
# Step 3: Inside the function, create a variable named total.
# Step 4: Use the formula:
# bill amount × (1 + tip percentage converted to decimal)
# Store the result in the total variable.
# Step 5: Round the value stored in total to 2 decimal places.
# Step 6: Display a message showing:
# "Please pay $<total amount>
# Step 7: End the function definition.
# --------------------------------------------------
# Step 8: Call the function.
# Step 9: Pass 150 as the bill amount.
# Step 10: Pass 20 as the tip percentage.
# Step 11: Run the program and observe the output."""
def total_calc(bill_amount, tip_percentage):
    total = bill_amount*(1+tip_percentage*0.01)
    total = round(total,2)
    print("Please pay $", total)
total_calc(150, 20)
