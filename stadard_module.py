import math
import random
import datetime

print(math.cos(0))

print(math.log10(100))

print(random.randint(1, 19))

print(random.uniform(0, 1))

today = datetime.datetime.now()
print(today)
print(today.strftime("%A, %B %dth %Y"))

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)

print(today - pi_day)

