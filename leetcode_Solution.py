#leetcode palindrome

#s = str(1234321)
# def F(s):
#    if len(s) <= 1:
#        return True
#    else:
#        if s[0] == s[-1]:
#            return F(s[1: -1])
#        else:
#            return False
#    return F(s)
#
# print(F(s))
#**************************************************************************
#leetcode N11
#h = [100, 8, 6, 20, 5, 4, 8, 3, 101]
#maxx, k = 0, 0
#max_k, max_z = 0, 0
#while k < len(h)-1:
#    for z in range(k+1, len(h)):
#        if h[k] > h[z]:
#            if h[z]*(z-k) > maxx:
#                maxx = h[z]*(z-k)
#                max_z = z
#                max_k = k
#        elif h[k] < h[z]:
#            if h[k]*(z-k) > maxx:
#                maxx = h[k]*(z-k)
#                max_z = z
#                max_k = k
#        else:
#            if h[k]*(z-k) > maxx:
#                maxx = h[k]*(z-k)
#                max_z = z
#                max_k = k
#    else:
#        k += 1
#print(maxx, max_k, max_z)
#*****************************************************************************
#leetcode N12
 
#
#def rom(x):
#    rom_num=''
#    s=str(x)[-1::-1]
#    for i in range(len(s)):
#        if int(s[i])<=3:     rom_num='I'*int(s[i])
#        elif int(s[i])==4:   rom_num='IV'    
#        elif int(s[i])==5:   rom_num='V'   
#        elif 5<int(s[i])<9:  rom_num='V'+'I'*(int(s[i])-5)
#        elif int(s[i])==9:   rom_num='IX'
#    print(rom_num)     
#
#rom(92346)
#


#****************************************************

#leetcode N14
# 
#strs = ["flllower","flllow","fllloight"]
#def F():
#    for i in range(1,10):
#        if strs[0][0:i]==strs[1][0:i]==strs[2][0:i]:
#            continue
#        else:return strs[0][0:i-1]
#
#print(F())          
#
#import random as rand
#import math

#leetcode N3    
def sort(s,lenght,k):
    if lenght==0:return 0
    else:
        for i in range(k):
            repeat=0
            for item in s[i:lenght+i]:
                if s[i:lenght+i].count(item)>1: 
                    repeat=1
            if not repeat:
                return lenght
        else:
            lenght-=1
            k+=1
            return sort(s,lenght,k)

#s="aa"
#s = "hijklmnopqrstuvwxyzA""BCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
s="khfkyusvneiwjcijajmbzjqiwzfnuhtgoaqmukhjrpfauojwzyxyhnjfooslxorlokzlwjunaanuqzq"
#s = "pwwkew"
#s="bbbbbb"
#s="abcabcghbb"
#s=""
#print(s[0:len(s)])
#s="a"
lenght=len(s)

if lenght>95:lenght=95

#print(lenght)
k=len(s)-lenght+1
#k=1
#print(k)
print(sort(s,lenght,k))


   