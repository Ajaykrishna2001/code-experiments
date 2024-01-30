#numbers in reverse

num=int(input("enter the number:"))
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("the rev order is:",rev)
 #palindrome in numbers
'''num=int(input("enter the number:"))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=int(num/10)
if temp==rev:
    
    print("the numbr is palindrome :")

else:
     print("the numbr is not palindrome :")'''
#swapping
'''a=5
b=8
temp=a
a=b
b=temp
print(a)
print(b)'''
#swapping without 3rd variable:
'''a=10
b=7
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''
#swap usg xor
'''a=10
b=7
a=a^b
b=a^b
a=a^b
print(a)
print(b)'''
#swap usg rotation cncpt
'''
a=5
b=6
a,b=b,a
print(a)
print(b)'''





