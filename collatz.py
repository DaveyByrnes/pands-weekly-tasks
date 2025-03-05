# collatz.py
# write a program that asks the user to input any positive interger and outputs
# successive values of the following calculation.
# at each step, calculate the next value by taking the current value and, if it is even
# divide it by two, but if it is odd, mulitply it by three and add one.
# author: David Byrne :)

def collatz(num): # define collatz as a function
    while num != 1:
        print(num)
        if num % 2 == 0: # divides even numbers by 2
            num = num // 2
        else:
            num = num * 3 + 1
    print(num)

num = int(input("Please enter a positive integer:"))
if num <=0:
    print("This number is not a positive interger. Please try again.")
else:
    collatz(num)