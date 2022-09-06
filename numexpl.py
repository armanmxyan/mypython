#!/bin/python3
#----------------------------
#
# Autor Arman Mkhitaryan 
# QUIZ | Python Day 1:
#
#---------------------------

#-- variables -----------------
_N = 1370
_N1000 = 0
_N100 = 0
_N10 = 0
_N1 = 0
Temp = 0

#---- calc 1000's ---------------

_N1000 = _N // 1000 
#print(_N1000)

#---- calc 100's ---------------

Temp =_N - 1000*_N1000
_N100  = Temp // 100
#print(_N100)

#---- calc 10's -----------------

Temp = Temp - 100*_N100
_N10   = Temp // 10
#print(_N10)

#----- calc 1's ------------------

_N1 = Temp - 10*_N10 
#print(_N1)

#-- printing -----------------

print('Origin Number is ' , _N)
print('1000s is ', _N1000)
print('100s is ' , _N100)
print('10s is ' , _N10)
print('1s is ',_N1)

#--- end off code -----------------------
