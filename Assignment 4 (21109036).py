# -*- coding: utf-8 -*-
"""Assignment 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nsVHllJRGYyEhFI5_Ax1i9tmw7UFR6SF
"""

#1
marks=float(input ("Enter your marks:"))
if marks>80:
 print('A')
elif marks in range (61,81):
 print('B')
elif marks in range (51,61):
 print('C')
elif marks in range (46,51):
 print('D')
elif marks in range (25,46):
 print('E')
else:
 print('F')

#2
year=int(input ("Enter the year:"))
if (year%4==0) and (year%100!=0):
  print(year,"is a leap year")
elif (year%100==0) and (year%400==0):
  print(year,"is a leap year")
else:
  print(year,"is not a leap year")

#3
import random as r
a=r.randint(1,40)
b=r.randint(1,15)
c=a*b
print(a,'*',b,'=')
d=int(input())
if d==c:
  print("Right")
else:
  print('Wrong. The answer is:',c)

#4
i=0
for i in range (201):
  if i%5==2:
    if i%6==3:
      if i%7==2:
        print(i, 'candies are in the bowl!')