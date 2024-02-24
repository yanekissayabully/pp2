#task 1

from datetime import *

now = datetime.now()

date2 = now - timedelta(days=5)
print("five days ago:", date2)

#task 2

from datetime import *

yesterday = now - timedelta(days=1)

tomorrow = now + timedelta(days=1)

print("yesterday:", yesterday)
print("today:", now)
print("tomorrow:", tomorrow)

#task 3

import datetime

today = datetime.datetime.now()
print(today) 
today = str(today)
woutmicro = today.split(".")
print(woutmicro[0])

#task 4

import datetime

class defDate:
    def __init__(self, date):
        self.date = datetime.timedelta(days = date)
        self.today = datetime.datetime.now()
    def secsdelta(self):
        date1 = self.today - self.date
        delta = self.today - date1        
        return delta.total_seconds()

date = defDate(int(input('Enter a date:\n')))

print(date.secsdelta())