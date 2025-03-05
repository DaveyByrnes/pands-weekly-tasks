# weekly task 05
# write a program that outputs whether or not today is a weekday.
# author: Dave Byrne :)

import datetime

# find current day
today = datetime.datetime.today().weekday()
# Monday = 0, Sunday = 6

# find if today is a weekday
if today < 5: # 0-4 are weekdays
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

