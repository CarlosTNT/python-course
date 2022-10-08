# modules

# own mules
# thirdy party modules
# python modules

import datetime
import fmath

print(fmath.add(12,7))
print(fmath.substract(20,10))


print(datetime.date.today())
print(datetime.timedelta(hours=50000))

from datetime import timedelta,date

print(date.today())
print(timedelta(minutes=180))

from fmath import substract,add

print(add(45,60))
print(substract(41,11))

import colorama
from colorama import Fore,Style

print(Fore.MAGENTA+"Hello world")