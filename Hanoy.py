from time import sleep
import sys
sys.setrecursionlimit(10000)


def move(n:int, x:list, y:list):
    global l_inst,l1,l2,l3,last_step
    
    if len(l2[1:])>=len(l_inst) or len(l3[1:])>=len(l_inst):
        return n ,l1[1:],l2[1:],l3[1:]    
    else:
        if y[-1]>x[-1] and x[-1]!=last_step:
            #y+=[x[-1]]
            last_step=x[-1]
            y.append(x[-1])
            x.pop(-1)
            n+=1              
            print(n,l1[1:],l2[1:],l3[1:])
            #return move(n, l1, l2) or move(n, l1, l3) or move(n, l2, l1) or move(n, l2, l3) or move(n, l3, l1) or move(n, l3, l2)
            #return move(n, l2, l1) or move(n, l2, l3) or move(n, l1, l2) or move(n, l1, l3) or move(n, l3, l1) or move(n, l3, l2)
            #return move(n, l3, l1) or move(n, l3, l2)or move(n, l1, l2) or move(n, l1, l3) or move(n, l2, l1) or move(n, l2, l3) 
            #return move(n, l1, l3) or move(n, l1, l2) or  move(n, l2, l3) or move(n, l2, l1) or move(n, l3, l2) or move(n, l3, l1) 
            return move(n, l1, l2) or move(n, l2, l3) or move(n, l1, l3) or move(n, l2, l1) or move(n, l3, l1) or move(n, l3, l2)
            #return move(n, l1, l2) or move(n, l1, l3) or move(n, l2, l1) or move(n, l2, l3) or move(n, l3, l1) or move(n, l3, l2)



l_inst=[x for x in range(6,0,-1)] #create Hanoy tower
#print(l_inst)
l1= [100]+l_inst
l2 = [100]
l3 = [100]
last_step=0
print(l1[1:],l2[1:],l3[1:],"     Start")
print(move(0,l1,l2),"   End")