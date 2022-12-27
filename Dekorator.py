#* Vasya *****************

# def Vasya(F):
#     #@functools.wraps(wrapped=func)
#     def wrapped():
#         i=input("How are you    ")
#         print("not good")
#         F()
#         return("BBB")
#     return wrapped    

# @Vasya
# def F():
#     print("AAA")    

# print(F())

#****** counter ************************

# from functools import wraps
# from time import sleep
# try:
#     f=open("count.txt","w")
#     print(f)
#     f.write("AAA") 
#     f.close()
# except:
#     print("Error")
# #else:
       
# finally:    
#     f.close()


# def counter(F):
#     @wraps(F)
#     def wrapped(*args):
        
#         x=""
#         try:   
#            f=open("count.txt",'r+')
#            x=f.readline()
#            #print(len(x))
#            print("zzz")
#            f.write("a")
#         except:
#             print("File open error")  
#             f=open("count.txt","w")
#             f.write("a") 
#             x="a"
#         finally:          
#             f.close()

#         return len(x)
#     return wrapped    

# @counter
# def F():
#     pass

# print(F())



# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped


# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# @makebold
# @makeitalic
# def hello():
#     return "hello habr"
# print (hello())  # выведет <b><i>hello habr</i></b>

#*** logging ****************************************
from functools import wraps
from  datetime import datetime
import traceback as tr
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        try:
            print(func.__name__ + " была исполнена")
            print(dir(func))
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            f=open("log.txt","a")
            f.write(func.__name__ + "," + str(datetime.now()) +
                    "," + str(e) +'\n')
            #f.write("AAA")
            f.close 
    return with_logging


@logit
def addition_func(x):
    """Считаем что-нибудь"""
    return x + x
result = addition_func(4)
print(result)

@logit
def substr(x,y):
    return x/y
result=substr(10,0)
print(result)


@logit
def divide(x, y):
    return x-y
result = divide("a", 5)
print(result)


@logit
def addition_func(x):
    """Считаем что-нибудь"""
    return x + x


result = addition_func(4)
print(result)

#**** delay ****************************
# from functools import wraps
# from time import sleep
# def counter(F):

#             @wraps(F)
#             def wraped(*args):
#                 sleep(5)
#                 return F()
#             return wraped    
# @counter
# def F():
#     return "AAA"

# print(F())
#***************************************************
#** counter  ****************************************
# class Decorator:
#     count = 0

#     def __init__(self, fun):
#         self._fun = fun

#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self._fun(*args, **kwargs)


# @Decorator
# def f(): 
#     pass
# f()
# f()

# f()
# print(f.count)
#***********************************************


