 
 
x=-123
 
if x < 0:
    s = str(x)
    x = -1*int(s[-1:-len(s):-1])
else:
    s=str(x)
    x=int(s[-1::-1]) 
print(x)


s = "the sky is  blue"
l=s.split(" ")
l=[x for x in l if x!='' ]
print(l)
w=""
l.reverse()
for st in l:
    #x=st.strip(" ")
    w=w+st+" "
else:
    #x=w.strip()
    print(w.strip())