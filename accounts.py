# accounts.py - weekly task 3
# create the program required for task 3
# by Dave Byrne :)

# prompt user
acc_num = (input("Please enter your 10 digit account number:"))

# slice the digits of the account number
anon_num = 'X' * 6 + acc_num[-4:] # negative indexing returns the last four digits

# print result
print(anon_num)