def F(n):
    if n ==0 or n==1:return 0
    else: 
        k=1
        if n==2:return k
        else:
            l=[x for x in range(3,n) if x&1==1]
            print(l)
            for x in l:
                for y in range(3,x,2):
                
                    if  x%y==0:
                        break
                else: 
                    k+=1
                    print(x)    
            else:return k
print(F(100))