'''double=lambda x:x*2
print (double(5))
def double(x):
  return x*2'''
'''
  #zoho qn
n=int(input("ENTER THE NUMBER"))
sum=0
count=0
while n>0:
    a=n%10
    sum=sum+a
    n=n/10
    count=count+1
sum=sum/count
print(sum)'''
    
    
'''my_list=[1,2,4,6,12,23,77,800,300,200]
new_list=list(filter(lambda x:(x%2==0.0),my_list))
print(new_list)'''

'''my_list=[1,2,4,6,12,23,77]
new_list=list(map(lambda x:x*2,my_list))
print(new_list)'''


'''x="global"

def foo():
    x="audi"
    print("x is inside:",x)
    
foo()'''


'''x="global"
def foo():
    global x #uding global keyword
    y="Local"
    x=x*2
    print(x)
    print(y)
foo()'''

'''x=8

def foo():
    x=25
    print("local x:",x)
    
foo()
print("global x:",x)'''

'''x="Local"

def inner():
    print("inner:",x*2)
    
inner()
print("outer:",x)'''


'''def outer_function():
    global a
    a=30
    
    def inner_function():
        global a
        a=70
        print("a=",a)
        
    inner_function()
    print("a=",a)
    
a=18
outer_function()
print("a=",a)'''
'''
#import math as m
from math import pi
from math import factorial
print(pi)
print(factorial(5))'''
'''
from decimal import Decimal  as D

print(D('1.1') +D('2.2'))
print(D('1.2') *D('2.50'))'''

#to find max num in array
arr=[30,34,20,13,4]
max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)

#to find min num in array
arr=[0,9,20,13,4]
min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        min=arr[i]
print(min)




