from random import randint,shuffle
#from bingo_check import check


def check(table):
    b, i, n, g, o, bingo, k = 0, 0, 0, 0, 0, 0, 0
    for x in table.keys():
        if sum(table[x]) == 0:
            return True
            break

        b += table[x][0]
        i += table[x][1]
        n += table[x][2]
        g += table[x][3]
        o += table[x][4]
        bingo += table[x][k]
        k += 1
    else:
        if (b and i and n and g and o and bingo):
            return False
        else:
            return True

#**********************************************************************
def gen(tbl):
   def rand(y):
      return [randint(1+15*y,15+15*y) for i in range(5)] 
   return {x:rand(y) for x,y in zip(tbl,range(len(tbl)))}

#**********************************************************************
def scr(table):
    print("\n")
    [print(i,end="  ") for i in table.keys()]
    k=0
    for k in range(5):
         print("\n")
         for symb in table.keys():
            if len(str(table[symb][k]))>1:
                print(str(table[symb][k]),end=" ")
            else:
                if table[symb][k]==0:
                    print("x",end="  ")
                else:    print(str(table[symb][k]),end="  ")    
                
    print("\n")

#***********************************************************************



def main():
    tbl=list("BINGO")
    table=gen(tbl)
    scr(table)
    box=[x for x in range(1,76)]
    shuffle(box)

    for x in box:
        for symb in tbl:
            if x in table[symb]: table[symb]=[y if y!=x else 0 for y in table[symb]]
        if check(table):
            scr(table)
            print("Yes BINGO")
            print("Iteration count  ",  box.index(x))
            print("\n")
            break


   # print(check(table))


#***********************************************************************************
if __name__ =="__main__":
   main()