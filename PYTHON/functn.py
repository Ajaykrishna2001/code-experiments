'''def absolute_value(num):
    if num>=0:
        return num
    else:
        return-num
print(absolute_value(2))
print(absolute_value(-4))'''

'''def my_fun():
    x=5
    print("the value of x:",x)
    
x=20
my_fun()
print(x)'''
'''
def outer_func():
    a=35
    
    def inner_func():
        a=7
        print("a=",a)
        
    inner_func()
    print('a=',a)
a=67
outer_func()
print(a)'''

'''
def outer(x,y):
    sum=x+y
    return sum
x=1
y=6
print("the sum is",outer(x,y))'''
'''
def call(name,msg):
    print("Hellow",name+','+msg)
call("gowtham","good nyt!")'''
'''
def greet(name, msg="Good morning!"):
    
    print("hellow",name+',' + msg)
greet("Kate")
greet("Bruce","how do you do?")'''
'''
def greet(*names):
    for name in names:
        print("Hellow",name)
greet("arul","mohan","reshi","gowtham")'''

def fun(x,y):
    if x==0:
        return y
    return fun(x-1,x+y)
print("Values:",fun(4,3))
    
    
    
    
    
    
    