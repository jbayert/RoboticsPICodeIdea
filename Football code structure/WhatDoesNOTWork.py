a = 5
def foo():
    a=6#a is now a local variable
    print("foo:",a)
def goo():
    print("goo:", a)#access a as a global variable

def loo():
    global a #all uses of a is global in this function
    print("loo:",a)
    a+=1
    print("loo2:", a)

def boo():
    print("boo:",a)#error cause it thinks a is a local variable
    a +=1

foo()#print new value 6
goo()#can access a global variable but it is stil 5

#This might work but seems more confusing 
#loo first prints 5, and then prints 6
loo()
print("Main:",a , "\n")#shows 6

boo()#error a is not defined

"""Output

foo: 6
goo: 5
loo: 5
loo2: 6
Main: 6 

Traceback (most recent call last):
  File "c:\Users\Jon B\Documents\Summer 2019\robotics\Football code structure\WhatDoesNOTWork.py", line 25, in <module>
    boo()
  File "c:\Users\Jon B\Documents\Summer 2019\robotics\Football code structure\WhatDoesNOTWork.py", line 15, in boo
    print("boo:",a)#error cause it thinks a is a local variable
UnboundLocalError: local variable 'a' referenced before assignment
"""
