#conversion btwn data type

'''num_int=12
num_flo=1.23
num_new=num_int+num_flo
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("datatype of num:",type(num_new))
print("value of num_new:",num_new)'''

'''num_int=123
num_str=float("456")
#sa=int(str)

print(type(num_int))
print(type(num_str))
print(num_int+num_str)
print(num_str)
#output formating'''

x=10
y=4
c=x+y
print("the value of sum {}".format(c))
print("the value of x is {} and y is {}".format(y,x))

print("my fav car {name} {model}".format(name='benz',model='AMG'))
print('I love {0} and {1}'.format('bread','butter'))

'''x=eval("5*3+6-1")
print(x)

num=input()
print(num)'''

'''import math
print(math.pi)
a=10
b=2
print(a*b)
print(a**b)
x=5
y=4
print(''x ** y''=,(x**y))'''

'''a=10
b=2
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

x=True
y=False
print(x and y)
print(x or y)
print (not x)'''

#identy operators in py
'''
x1=4
y1=4
x2='Audi'
y2='Audi'
x3=[1,2,3]
y3=[1,2,3]

print(x1 is not y1)

print(y2 is x2)

print(x3 is y3)
print(id(x1))
print(id(y2))'''