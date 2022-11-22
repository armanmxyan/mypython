#m = [[1,2,3],[4,5,6],[7,8,9]]
matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
m=matrix
print(m[0])
print(m[1])
print(m[2])
print(m[3])
#print("\n")
#m[0][2], m[2][2], m[2][0], m[0][0]= m[0][0], m[0][2], m[2][2], m[2][0]
#print(m[0])
#print(m[1])
#print(m[2])

def F(m):
    
    lm=len(m)
    
    for n in range(0,lm//2):
        for x in range(n,lm-n):
            print(n,x+n,1)
            m[n][x], m[x][n] = m[x][n], m[n][x]
            if x>n:
                print(x,lm-1-n,2)
                m[x][lm-1-n], m[lm-1-n][x] = m[lm-1-n][x], m[x][lm-1-n]

    '''  
        for x in range(1,lm-1):                                            
            m[1][x],m[x][1]=m[x][1],m[1][x]                        
            if x>1:
                m[x][lm-2],m[lm-2][x]=m[lm-2][x],m[x][lm-2]
    '''
    
    
    
    for i in range(0,len(m)):
        m[i].reverse()

F(m)
print("\n")
print(m[0])
print(m[1])
print(m[2])
print(m[3])