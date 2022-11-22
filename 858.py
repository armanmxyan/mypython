        
def F(p,q):        
    n=0
    while n<1000:
        print(n)
        if (p+2*n*p)%(2*q)==0: 
            return 2 
            break            
        elif ((p+2*n*p)-q)%(2*q) ==0 : 
            return 1
            break
        elif n>0:
                if(n*2*p-q)%(2*q)==0 :
                    return 0
                    break
        n+=1 


print(F(5,4))        