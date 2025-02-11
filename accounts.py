# accounts.py - weekly task 3
# create the program required for task 3
# by Dave Byrne :)

# extra requirements

# I am assuming I need to find a way to make 'x' * 6 more flexible to allow for 'X' + any number.
# There's probably a trick to it with indexing that I'm going to research.
# discovered the solution through googling - https://www.pythoncheatsheet.org/cheatsheet 
# I am going to use the len() function

# old approach: hardcoded 'X' length, new approach is dynamic using len()

# prompt user
acc_num = (input("Please enter your account number:")) # changed prompt from '10 digit number' to 'number' to avoid confusion

# slice all but the last four digits
anon_num = 'X' * (len(acc_num) - 4) + acc_num[-4:] # all but 4 digits are replaced with X, negative indexing used to find last four digits

# print result
print(anon_num)