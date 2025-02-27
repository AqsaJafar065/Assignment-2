Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #get user input
>>> num=float(input("enter a number:"))
enter a number:-3
>>> if num>0:
...     print("the number is positive")
... elif num<0:
...     print("the number is negative")
... else:
...     print("the number is zero")
... 
...     
the number is negative
>>> 
>>> 
>>> #get user input
>>> year=int(input("enter a year:"))
enter a year:2012
>>> if year%4==0 and (year%100!=0 or year%400==0):
...     print(f"{year} is a leap year")
... else:
...     print(f"{year} is not a leap year")
... 
...     
2012 is a leap year
