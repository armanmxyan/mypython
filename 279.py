
def F(n):
    x,k=1,1
    l=[]
    l1=[]
    l2={ 0,}
    while x**2<=n:
        l.append(x**2)
        if x**2==n:
            return k
        x+=1
        
    l1=l.copy()    
    
    def F(l1,l,k):
        for i in range(len(l)):
            for j in range(len(l1)):
                if l[i]+l1[j]==n:return k+1
                else:
                    if l[i]+l1[j]<n:

                        l2.add(l[i]+l1[j])
                        #l2.sort()
        else:
            #print(l2)
            l1=list(l2)
            print(l1)            
            return F(l1,l,k+1)    
                       
    return(F(l1,l,k))

print(F(1333))        