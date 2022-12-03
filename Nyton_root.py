

#ai+1=0.5*(ai+x/ai)
x=121.0
a=x/2

#print(10**(-2))
while abs(x-a**2)>1e-12:
    print(a)
    a=(a+x/a)/2
else: print(a)    


def root(x,a):
    
    if abs(x-a**2)<1e-12:
        return a
    else: 
        a=(a+x/a)/2

        return root(x,a) 
                    
print(root(x,a))    

s=""
def dec_to_bin(x):
    global s
    if x==1:return s+"11"         
    elif x==2: return s+"01"
    else: 
        if x%2 > 0: s+="1"     
        else: s+="0"    
        return dec_to_bin(x//2)
   
x=8
print("0b"+dec_to_bin(x)[-1::-1])    





def unpack(l):
    print(l)
    if l==[]:
        print(l)
        return []
    elif isinstance(l[0],list):
        return unpack(l[0]) + unpack(l[1:])
    else:
        return [l[0]] + unpack(l[1:])    
        

l=[[1], [2, 3], [[4, 5, [6, 7]]], [[[8], 9], [10]]] 
print(unpack(l))
