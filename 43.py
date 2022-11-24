num1='226'
num2='456'
s="123"
l1=list(num1[-1::-1])
l2=list(num2[-1::-1])

n1,n2=0,0
for x in range(len(l1)):
    print(ord(l1[x])-48)
    n1=n1+(ord(l1[x])-48)*(10**x)

for x in range(len(l2)):
    print(ord(l2[x])-48)
    n2 = n2+(ord(l2[x])-48)*(10**x)

print(str(n1+n2))
print(ord('0'))
print(l1,l2)