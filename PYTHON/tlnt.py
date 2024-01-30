#membership operator

'''x='Hello wprld'
y={1:'a',2:'b'}

print('H' in x )
print('hellow' not in x)
print('a' in y )
print(1 in y)'''

'''a=5
print(id(a))
a=9
print(id(a))
a=5
print(id(a))
b=5
print(id(b))'''

'''c=8
print(id(c))
print(id(8))

a=2
print('id(a)=',id(a))

a=1+a
print('id(a)=',id(3))

def outer_function():
    a=50
    
    def inner_function():
        a=25
        print('a=',a)
        
    inner_function()
    print('a=',a)
    
    
a=15       #global fn
outer_function()
print('a=',a)'''

'''numbers=[2,5,9,3,12,7,6]
sum=0
for val in numbers:
    #sum+=val
    sum=sum+val 
print("The sum is",sum)'''

'''print (range(10))
print(list(range(10)))
print(list(range(2,8)))'''




n=int(input("entr num:"))
temp=n
rev=0
while n >0:
    dig=n%10
    rev=rev*10+dig
    n=int(n/10)
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")
    
    


    





    

    







