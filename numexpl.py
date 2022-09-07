#!/bin/python3

#*****************************
#
# Autor Arman Mkhitaryan 
# QUIZ | Python Day 1:
#
#****************************

#**** Data *************

N = 1370

#**** calc 1000's ***********

N1000 = N // 1000 
Temp = N % 1000

#**** calc 100's ************

N100  = Temp // 100
Temp = N % 100

#**** calc 10's *************

N10   = Temp // 10

#*** calc 1's **************

N1 = Temp % 10 

#*** Print ****************

print('Origin Number is ' , N)
print('1000s is ',  N1000)
print('100s is  ',  N100)
print('10s is   ',  N10)
print('1s is    ',  N1)

#*** end programm ***********
