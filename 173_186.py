#== Ex 185 ==============
'''
l = ["A", 12, "B", 4, "A", 6, "B", 1]
l_dec=[]
def F(l):
    pass
    if l[1]+l[3]+l[5]+l[7]==0:
        return l_dec
    else:
        if l[1]>0:
            l_dec.append("A")
            l[1]-=1
            return F(l)
        elif l[3]>0:
            l_dec.append("B")
            l[3]-=1
            return F(l)
        elif l[5]>0:
            l_dec.append("A")
            l[5]-=1
            return F(l)
        elif l[7]>0:
            l_dec.append("B")    
            l[7]-=1
            return F(l)

print(F(l))    

#== Ex186 ===================================

def F(x,y):
     
    if len(x)==0:
        return y
    else:
        i=0
        while  x[i] == x[0]:
            i+=1
            if i>=len(x):break
                    
        y.append(x[i-1])
        y.append(i)
        return F(x[i:],y)    
    


x = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
    'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B']
y=[]    
print(F(x,y))
'''

#== Ex181 ========================================
 
i = input("input summ and coins quantity ").split(",")  
#l=[1,5,10,25] 
summ=int(i[0]) 
coins=int(i[1])
d5,d10,d25=0,0,1 #directs

def F(x,y,z):
    global summ,coins,d5,d10,d25
    print(summ,coins)
    c=coins-(x+y+z) #  nominal"1"  coins remainder
    s=c+5*x+10*y+25*z  # summ counter
    print(s,c,x,y,z)
    
    if s==summ:  # if have summ ret true
        print(c,x,y,z)     
        return True
        
    else:
        if c>0 :
            if s<summ:
                return F(x+d5,y+d10,z+d25)   # increase wiht directs    
            else:
                if d25: # if summ counter s > summ,decrease at 25 and enable 10th increaser
                    d25=0
                    d10=1
                    if z>0:z-=1    
                    return F(x+d5,y+d10,z+d25) 
                    
                elif d10:  # if summ counter s > summ,decrease at 10 and enable 5th increaser
                    d10=0
                    d5=1
                    if y>0:y-=1
                    return F(x+d5,y+d10,z+d25) 
                    
                elif d5:  # if summ counter s > summ,decrease at 10 and increase at 5
                    #d5=0
                    if y>0:y-=1
                    elif y==0:# then 10th coins =0,decrease  at 25 ,and run cicle again from d10 increaser
                        z-=1
                        x=0
                        d5=0
                        d10=1
                    return F(x+d5,y+d10,z+d25) 




if 25*coins<summ or coins>summ:
    print(False)
else:        
    x,y,z=0,0,0
    print(F(x,y,z))






