# bank.py - weekly task 2
# create the bank program required for task 2
# by Dave Byrne :)

# prompt user
num1_cents = float(input("Enter the first amount(in cents):"))
num2_cents = float(input("Enter the second amount(in cents):"))

# add amount
total_cents = num1_cents + num2_cents

# convert cents to euros
total_euros = total_cents / 100 # divide to get a float

# print result

print("The total amount is: €", total_euros)