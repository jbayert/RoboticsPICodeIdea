a = 5
def foo():
    a=6#a is now a local variable
    print("foo:",a)
def goo():
    print("goo:", a)#access a as a global variable
def boo():
    print("boo:",a)#error cause it thinks a is a local variable
    a +=1

foo()#print new value 6
goo()#can access a global variable but it is still 5
boo()

