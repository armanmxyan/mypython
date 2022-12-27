#***N1*****************************

# my_ls=[[i,i+4,i+8] for i in range(1,5)]
# print(my_ls)

#**N2******************************
# my_ls=[0,2,1,0,0,0,1,0,2,0]
# for x in my_ls:
#     if x==0:
#         my_ls.remove(x)
#         my_ls.append(x)
# else:print(my_ls)
    
# for x in range(len(my_ls)):
#     if my_ls[x]==0:break   
# print(my_ls[:x])
#** N3 *******************************
# alphabet="abcdefg"
# my_str=alphabet
# print(my_str)
# print(alphabet[-1::-1])
# print(alphabet[0::2])
# print(alphabet[1::2])
# print(alphabet[:1])
# print(alphabet[-1:-2:-1])
# print(alphabet[3:4])
# print(alphabet[-3:])
# print(alphabet[3:5])
# print(alphabet[4:2:-1])


#**N5******************************

# my_dict={"Привет":"Здравствуйте","Печально":"Грустно","Весело":"Радостно"}

# i=input("insert word  ")
# for x in my_dict.keys():
#     if x==i:
#         print(my_dict[x])
#         break
# else:print("Такого слова нет")    

#**N4***************************************
#print(int(0x410))
# rus_vowels_unicode = ([0x410, 0x430, #A,a
#           0x415, 0x435,  #Е,е
#           0x418, 0x438,  #И,и
#           0x41E, 0x43E,  # О,о
#           0x423, 0x443,  # У,у
#           0x42D, 0x44D,  # Э,э
#           0x42B, 0x44B,  # Ы,ы
#           0x401, 0x451,  # Ё,ё
#           0x42F, 0x44F,  # Я,я
#           0x42E, 0x44E])  # Ю,ю
# vowels_list=[]
# i=input("insert Russian text   "  )
# for x in i:
#     if ord(x) in rus_vowels_unicode:
#         vowels_list.append(x)
# else:print(vowels_list)

#** N7 ******************************************


# def isprime(in_iter)->list:
#     prime=[]
#     for x in in_iter:
#         for y in range(2,len(x)):
#             if ord(x)%y==0:break
#         else: prime.append(x)
#     else:return prime

# def cripto(in_iter):
#     return isprime(in_iter)

# print(cripto([0,1,2,3,4,5,6,7,8,9]))

#**N8******************

# def F(tup:tuple,symb:any)->tuple:
#     lindex,rindex=0,0
#     try:
#         lindex=tup.index(symb)
#     except ValueError:
#         return tup[0:0]
    
#     try: 
#         rindex=tup[lindex+1:].index(symb)       
#     except ValueError:
#         return tup[lindex:]
    
#     return tup[lindex:lindex+rindex+2]

# print(F((2,1,2,3,5,6,48,0,0,4,5),2) )   

#**N9*****************

# import random
# my_ls=[random.randint(1,10) for i in range(10)]
# print(my_ls)
# [my_ls.append((my_ls[i],my_ls[i+1])) for i in range(0,9,2)]
# my_ls=my_ls[-5::1]
# print(my_ls)

#**10**********************************

# st="abcde"
# t=[10,20,30,40,50,60]
# #[print((st[i],t[i])) for i in range(len(st))]

# def ziper(iter1:iter,iter2:iter)->tuple:
#     l=min(len(iter1),len(iter2))
#     return tuple([(iter1[i], iter2[i])  for i in range(l)])
# print(ziper(st,t))

#**N11*******************************

# def F(n):
#     if n==0: 
#         print(10-n)
#         return
#     else:
#         print(10-n)
#         return F(n-1)    
# F(10)

#**N12 ***********************


# st="abcde"
# t=[10,20,30,40,50,60]
# ss=(1,5,2)
# #[print((st[i],t[i])) for i in range(len(st))]

# def ziper(*iter1:iter)->tuple:
#     print(*iter1)
#     #l= *iter1.count(*)
#     print(*iter1[2])
#     #return tuple([(iter1[i], iter2[i])  for i in range(l)])
# print(ziper(st,t,ss))

#** N13 ************************************

# def calc_math_func(data):
#     res=1
#     for index in range(1,data+1):
#         res*=index
#     res/=data**3
#     res=res**10
#     return res

#** N14 *******************************

# def summer(x)->int:
#     y=[]   
#     for i in x:     
#         if isinstance(i,list) or isinstance(i,tuple)  :
#             y+=i
#         elif isinstance(i,int) or isinstance(i,float): 
#             y.append(i)           
#             if x.index(i)==len(x)-1:
#                 print(y)
#                 return sum(y)
        
#     else: return summer(y)   
# #print(summer([1,2,[3,4],[5,6,[7,[8],[9,10]]]]))    
# print(summer((1, 2, (3, 4), (5, 6, (7, (8), (9, 10))))))
# #print(summer({1, 2, {3, 4}, {5, 6, {7, {8}}}}))

#**N15****************************************
# from time import sleep
# import sys
# sys.setrecursionlimit(10000)


# def move(n:int, x:list, y:list):
#     global l_inst,l1,l2,l3,last
    
#     if len(l2[1:])>=len(l_inst) or len(l3[1:])>=len(l_inst):
#         return n ,l1[1:],l2[1:],l3[1:]    
#     else:
#         if y[-1]>x[-1] and x[-1]!=last:
#             y.append(x[-1])
#             last=x[-1]
#             x.pop(-1)
#             n+=1              
#             print(n,l1,l2,l3)
#             #return move(n, l1, l2) or move(n, l1, l3) or move(n, l2, l1) or move(n, l2, l3) or move(n, l3, l1) or move(n, l3, l2)
#             #return move(n, l2, l1) or move(n, l2, l3) or move(n, l1, l2) or move(n, l1, l3) or move(n, l3, l1) or move(n, l3, l2)
#             #return move(n, l3, l1) or move(n, l3, l2)or move(n, l1, l2) or move(n, l1, l3) or move(n, l2, l1) or move(n, l2, l3) 
#             #return move(n, l1, l3) or move(n, l1, l2) or  move(n, l2, l3) or move(n, l2, l1) or move(n, l3, l2) or move(n, l3, l1) 
#             return move(n, l1, l2) or move(n, l2, l3) or move(n, l1, l3) or move(n, l2, l1) or move(n, l3, l1) or move(n, l3, l2)
#             #return move(n, l1, l2) or move(n, l1, l3) or move(n, l2, l1) or move(n, l2, l3) or move(n, l3, l1) or move(n, l3, l2)



# l_inst=[x for x in range(6,0,-1)]
# l1= [100]+l_inst
# l2 = [100]
# l3 = [100]
# #l_inst=l_inst[1:]
# print(l1,l3,l3)
# print(l_inst)
# last=0

# print(move(0,l1,l2))

#** N16 *******************************************
import collections
class Stack:
    def __init__(self) -> None:
        self.task_dict={}
        self.d={}
    def stack_store(self,TaskPriority:int,TaskName:str):
        if TaskPriority in self.task_dict.keys():
            self.task_dict[TaskPriority] = self.task_dict[TaskPriority]+[TaskName]
        else:
           self.task_dict.setdefault(TaskPriority,[TaskName])
        

    def del_task(self, TaskPriority: int, TaskName: str):
        #try:
        if TaskPriority in self.task_dict.keys():
            if TaskName in   self.task_dict[TaskPriority] :
                self.task_dict[TaskPriority].remove(TaskName)
            else:print(f" {TaskName} Task non exist for remove")
        else:print(f" N{TaskPriority} Priority non exist for remove")    

        #except: print("Task non exist")

    def get_task(self):
        return self.task_dict

class TaskManager:
    def __init__(self) -> None:
        self.dict_str=""

    def __str__(self) -> str:
        str1=""
        task_dict = p.get_task()
        self.dict_str=""
        for x in sorted(task_dict.keys()):
            str1=""
            for y in task_dict[x]:
                str1=str1+y+" "
            self.dict_str= self.dict_str + f"{x} {str1}\n"
        
        else:return self.dict_str
            
    
    def new_task(self,TaskName:str,TaskPriority:int):
        p.stack_store(TaskPriority,TaskName)        

    def del_task(self, TaskName: str, TaskPriority: int):
        p.del_task( TaskPriority,TaskName )



p=Stack()
manager=TaskManager()
manager.new_task("Restart",6)
manager.new_task("Move File", 2)
manager.new_task("Install Programm",4)
manager.new_task("Save File", 4)
manager.new_task("Open File", 1)
manager.new_task("Remove",7)
print(manager)
#manager.del_task("BBB",4)
manager.del_task("Save File",5)
manager.del_task("Install Programm",4)
print(manager)











