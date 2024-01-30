#stars
'''
a=int(input("Enter a value="))
for i in range(a-1,0,+1):
    for j in range(i+1):
        print("*",end="")
        print("\n")
    
for i in range(a+1,0,-1):
    for j in range(i-1):
        print("*",end="")
    print("\n")  '''
    
'''
#palindrome in numbers
n=int(input("enter the number"))
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=int(n/10)
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")'''
#fibonosis 
'''
n=int(input ("enter the number="))
a=0
b=1
for i in range(n):
    print(a)
    temp=a
    a=b
    b=temp+b'''














   