# -*- coding: utf-8 -*-
"""Challenge1..2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DIlIddrHqJ4ma98gs7eXWEAa8bK1ARLH
"""

def isLeapyear(year):
  if(year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
    return True
  else:
    return False
year =int(input("Enter a year:"))
if isLeapyear (year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))

